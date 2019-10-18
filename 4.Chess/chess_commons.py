from __future__ import annotations

from copy import deepcopy
from enum import Enum
from typing import Optional
from itertools import groupby


class ChessError(Exception):
    """
    Base exception class for chess utilities.
    """


class Figure(Enum):
    W_KING = 'K'
    W_QUEEN = 'Q'
    W_BISHOP = 'B'
    W_ROOK = 'R'
    W_KNIGHT = 'N'
    W_PAWN = 'P'

    B_KING = 'k'
    B_QUEEN = 'q'
    B_BISHOP = 'b'
    B_ROOK = 'r'
    B_KNIGHT = 'n'
    B_PAWN = 'p'


class Column(Enum):
    a = 97
    b = 98
    c = 99
    d = 100
    e = 101
    f = 102
    g = 103
    h = 104

    @property
    def left(self):
        if self is Column.a:
            return None
        else:
            return Column(self.value - 1)

    @property
    def right(self):
        if self is Column.h:
            return None
        else:
            return Column(self.value + 1)

    def __str__(self):
        return self.name

    @classmethod
    def names(cls):
        return tuple(cls.__members__.keys())


EMPTY_SQUARE = '.'
FIGURES = set(Figure)


class Turn(Enum):
    WHITES = 'w'
    BLACKS = 'b'


BORDER_LINE = '  +-----------------+'
EMPTY_DATA = '-'


def split_fen_string(fen_string, with_end=True):
    lines = fen_string.split('/')
    turn = None
    castling = None
    en_passant = None
    half_moves = None
    full_moves = None
    if with_end:
        last_line, turn, castling, en_passant, half_moves, full_moves = lines[-1].split(' ')
        lines[-1] = last_line
    return lines, turn, castling, en_passant, half_moves, full_moves


def represent_fen_lines(lines):
    output_lines = [BORDER_LINE]
    for j, line in zip(reversed(range(1, 9)), lines):
        out_line = ''
        for s in line:
            out_line += '.' * int(s) if s.isdigit() else s
        output_lines.append(f'{j} | {" ".join(out_line)} |')
    output_lines.append(BORDER_LINE)
    output_lines.append(f'    {" ".join(Column.names())}  ')
    return '\n'.join(output_lines) + '\n\n'


class Position(object):

    def __init__(self, fen_input_string):
        self.castling_map = {
            Figure.W_KING: False,
            Figure.W_QUEEN: False,
            Figure.B_KING: False,
            Figure.B_QUEEN: False
        }
        raw_lines, turn, castling, en_passant, half_moves, full_moves = split_fen_string(fen_input_string)
        self.turn = Turn(turn.lower())
        if castling != EMPTY_DATA:
            for c in castling:
                self.castling_map[Figure(c)] = True
        self.en_passant = en_passant if en_passant != EMPTY_DATA else None
        self.half_moves = int(half_moves)
        self.full_moves = int(full_moves)
        self.lines = Position._convert_raw_lines(raw_lines)

    @classmethod
    def _convert_raw_lines(cls, raw_lines):
        lines = []
        column_names = Column.names()
        for line in raw_lines:
            if not line:
                lines.append({c: None for c in Column})
                continue
            converted_line = {}
            position_pointer = 0
            for s in line:
                if s.isdigit():
                    for c in column_names[position_pointer: position_pointer + int(s)]:
                        converted_line[Column(ord(c))] = None
                    position_pointer += int(s)
                else:
                    converted_line[Column(ord(column_names[position_pointer]))] = Figure(s)
                    position_pointer += 1
            if position_pointer != 8:
                for c in column_names[position_pointer: 8]:
                    converted_line[c] = None
            lines.append(converted_line)
        lines.reverse()
        return lines

    def _count_move(self, row_from: int, col_from: Column, row_to: int, col_to: Column) -> None:
        if self.turn == Turn.BLACKS:
            self.full_moves += 1
            self.turn = Turn.WHITES
        else:
            self.turn = Turn.BLACKS
        self.half_moves += 1
        capture = self._at_cell(col_to, row_to) in FIGURES
        pawn_move = self._at_cell(col_from, row_from) in [Figure.B_PAWN, Figure.W_PAWN]
        if pawn_move or capture:
            self.half_moves = 0

    def _check_en_passant(self, row_to: int, col_to: Column) -> None:
        figure_to = self._at_cell(col_to, row_to)
        figure_above = self._at_cell(col_to, row_to + 1)
        figure_below = self._at_cell(col_to, row_to - 1)
        if figure_to == Figure.B_PAWN and figure_above == Figure.W_PAWN:
            self.lines[row_to + 1][col_to] = None
        elif figure_to == Figure.W_PAWN and figure_below == Figure.B_PAWN:
            self.lines[row_to - 1][col_to] = None

    def _set_en_passant(self, row_to: int, col_to: Column) -> None:
        pawn = self._at_cell(col_to, row_to)
        target_row = row_to - 1 if self._at_cell(col_to, row_to) == Figure.W_PAWN else row_to + 1
        on_the_left = self._at_cell(col_to.left, row_to) if col_to.left else None
        on_the_right = self._at_cell(col_to.right, row_to) if col_to.right else None
        opposite_pawn_on_the_left = on_the_left in (Figure.W_PAWN, Figure.B_PAWN) and on_the_left != pawn
        opposite_pawn_on_the_right = on_the_right in (Figure.W_PAWN, Figure.B_PAWN) and on_the_right != pawn
        if any((opposite_pawn_on_the_left, opposite_pawn_on_the_right)):
            self.en_passant = f"{col_to}{target_row+1}"
        else:
            self.en_passant = None

    def move(self, cell_from: str, cell_to: str) -> Position:
        row_from, col_from = int(cell_from[1]) - 1, Column(ord(cell_from[0]))
        row_to, col_to = int(cell_to[1]) - 1, Column(ord(cell_to[0]))
        new_position = deepcopy(self)
        new_position._count_move(row_from, col_from, row_to, col_to)
        new_position.lines[row_to][col_to] = new_position.lines[row_from][col_from]
        new_position.lines[row_from][col_from] = None
        if cell_to == self.en_passant:
            new_position._check_en_passant(row_to, col_to)
        if new_position._at_cell(col_to, row_to) in (Figure.W_PAWN, Figure.B_PAWN) and abs(row_from - row_to) == 2:
            new_position._set_en_passant(row_to, col_to)
        else:
            new_position.en_passant = None
        if len(cell_to) == 3:
            # pawn transformation
            new_position.lines[row_to][col_to] = Figure(cell_to[2])
        return new_position

    def _at_cell(self, col: Column, row: int) -> Optional[Figure]:
        return self.lines[row][col]

    def at_cell(self, cell_string: str) -> Optional[Figure]:
        if len(cell_string) != 2 or not cell_string[1].isdigit():
            raise ChessError("Cell address must be a character a-h and a digit 1-8.")
        row = int(cell_string[1]) - 1
        col = Column(ord(cell_string[0]))
        return self.lines[row][col]

    def to_fen_string(self) -> str:
        fen_lines = []
        for line in reversed(self.lines):
            # that could have been more readable but I was too keen to use one-liners in the recreational coding
            # in effect, itertools.groupby just gives an item:iterator[over same items in a row] for item in a sequence
            fen_lines.append(''.join(''.join(e.value for e in elements) if key else str(len(list(elements)))
                                     for key, elements in groupby(line.values())))
        castling_data = (''.join(sorted(k.value if v else '' for k, v in self.castling_map.items()))
                         if any(self.castling_map.values()) else EMPTY_DATA)
        return f"{'/'.join(fen_lines)} {self.turn.value} {castling_data} {self.en_passant or EMPTY_DATA}" \
               f" {self.half_moves} {self.full_moves}\n"

    def __str__(self):
        output_lines = [BORDER_LINE]
        for j, line in zip(reversed(range(1, 9)), reversed(self.lines)):
            output_lines.append(f'{j} | {" ".join(s.value if s else "." for s in line.values())} |')
        output_lines.append(BORDER_LINE)
        output_lines.append(f'    {" ".join(Column.names())}  ')
        return '\n'.join(output_lines) + '\n\n'
