from __future__ import annotations

from copy import deepcopy
from enum import Enum
from typing import Optional, List, Tuple
from itertools import groupby


class ChessError(Exception):
    """
    Base exception class for chess utilities.
    """


def set_bit(int_type, offset):
    mask = 1 << offset
    return int_type | mask


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

    @staticmethod
    def figures():
        return set(Figure)

    @staticmethod
    def pawns():
        return Figure.W_PAWN, Figure.B_PAWN

    @staticmethod
    def knights():
        return Figure.W_KNIGHT, Figure.B_KNIGHT

    @staticmethod
    def rooks():
        return Figure.W_ROOK, Figure.B_ROOK

    @staticmethod
    def bishops():
        return Figure.W_BISHOP, Figure.B_BISHOP

    @staticmethod
    def queens():
        return Figure.W_QUEEN, Figure.B_QUEEN

    @staticmethod
    def kings():
        return Figure.W_KING, Figure.B_KING


WHITES = (Figure.W_KING, Figure.W_QUEEN, Figure.W_ROOK, Figure.W_BISHOP, Figure.W_KNIGHT, Figure.W_PAWN)
BLACKS = (Figure.B_KING, Figure.B_QUEEN, Figure.B_ROOK, Figure.B_BISHOP, Figure.B_KNIGHT, Figure.B_PAWN)


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


DEFAULT_CELLS = {
    Figure.B_KING: (Column.e, 7),
    Figure.W_KING: (Column.e, 0),
    Figure.B_ROOK: ((Column.a, 7), (Column.h, 7)),
    Figure.W_ROOK: ((Column.a, 0), (Column.h, 0))
}

CASTLING_CELLS = {
    Figure.W_KING: ((Column.c, 0), (Column.g, 0)),
    Figure.B_KING: ((Column.c, 7), (Column.g, 7)),
    Figure.B_ROOK: ((Column.d, 7), (Column.f, 7)),
    Figure.W_ROOK: ((Column.d, 0), (Column.f, 0))
}


EMPTY_SQUARE = '.'
EMPTY_BOARD_FEN = '8/8/8/8/8/8/8/8 w - - 0 0'


class Turn(Enum):
    WHITES = 'w'
    BLACKS = 'b'


BORDER_LINE = '  +-----------------+'
EMPTY_DATA = '-'


def get_cell_number(col: Column, row: int) -> int:
    return 8 * row + col.value - 97


def get_cell_for_number(number: int) -> Tuple[Column, int]:
    row = number // 8
    col = Column(number % 8 + 97)
    return col, row


def split_fen_string(fen_string, with_end=True):
    lines = fen_string.split('/')
    turn = 'w'
    castling = EMPTY_DATA
    en_passant = EMPTY_DATA
    half_moves = 0
    full_moves = 0
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

    def __init__(self, fen_input_string, with_end=True):
        self.castling_map = {
            Figure.W_KING: False,
            Figure.W_QUEEN: False,
            Figure.B_KING: False,
            Figure.B_QUEEN: False
        }
        raw_lines, turn, castling, en_passant, half_moves, full_moves = split_fen_string(fen_input_string, with_end)
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

    def _count_move(self, col_from: Column, row_from: int, col_to: Column, row_to: int) -> None:
        if self.turn == Turn.BLACKS:
            self.full_moves += 1
            self.turn = Turn.WHITES
        else:
            self.turn = Turn.BLACKS
        self.half_moves += 1
        capture = self._at_cell(col_to, row_to) in Figure.figures()
        pawn_move = self._at_cell(col_from, row_from) in Figure.pawns()
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
        opposite_pawn_on_the_left = on_the_left in Figure.pawns() and on_the_left != pawn
        opposite_pawn_on_the_right = on_the_right in Figure.pawns() and on_the_right != pawn
        if any((opposite_pawn_on_the_left, opposite_pawn_on_the_right)):
            self.en_passant = f"{col_to}{target_row+1}"
        else:
            self.en_passant = None

    def _check_castling(self, removed_figure: Optional[Figure], moved_figure: Figure, col_from: Column, row_from: int,
                        col_to: Column, row_to: int) -> None:
        cell_from, cell_to = (col_from, row_from), (col_to, row_to)
        if moved_figure == Figure.W_KING and cell_from == DEFAULT_CELLS[Figure.W_KING]:
            self._do_castling(col_to, row_to, moved_figure, Figure.W_QUEEN, Figure.W_ROOK)
        elif moved_figure == Figure.B_KING and cell_from == DEFAULT_CELLS[Figure.B_KING]:
            self._do_castling(col_to, row_to, moved_figure, Figure.B_QUEEN, Figure.B_ROOK)
        for rook, queen, king in ((Figure.W_ROOK, Figure.W_QUEEN, Figure.W_KING),
                                  (Figure.B_ROOK, Figure.B_QUEEN, Figure.B_KING)):
            rook_cell = cell_from if rook == moved_figure else cell_to if rook == removed_figure else None
            if rook_cell:
                if rook_cell == DEFAULT_CELLS[rook][0]:
                    self.castling_map[queen] = False
                elif rook_cell == DEFAULT_CELLS[rook][1]:
                    self.castling_map[king] = False

    def _do_castling(self, col_to: Column, row_to: int, king: Figure, queen: Figure, rook: Figure) -> None:
        if (col_to, row_to) == CASTLING_CELLS[king][0] and self.castling_map[queen]:
            self._move_figure(*DEFAULT_CELLS[rook][0], *CASTLING_CELLS[rook][0])
        elif (col_to, row_to) == CASTLING_CELLS[king][1] and self.castling_map[king]:
            self._move_figure(*DEFAULT_CELLS[rook][1], *CASTLING_CELLS[rook][1])
        self.castling_map[king] = False
        self.castling_map[queen] = False

    def move(self, cell_from: str, cell_to: str) -> Position:
        row_from, col_from = int(cell_from[1]) - 1, Column(ord(cell_from[0]))
        row_to, col_to = int(cell_to[1]) - 1, Column(ord(cell_to[0]))
        new_position = deepcopy(self)
        new_position._count_move(col_from, row_from, col_to, row_to)
        new_position._move_figure(col_from, row_from, col_to, row_to)
        if any(self.castling_map.values()) and (self._at_cell(col_from, row_from) in Figure.rooks() + Figure.kings()
                                                or self._at_cell(col_to, row_to) in Figure.rooks()):
            new_position._check_castling(self.lines[row_to][col_to], self.lines[row_from][col_from],
                                         col_from, row_from, col_to, row_to)
        if cell_to == self.en_passant:
            new_position._check_en_passant(row_to, col_to)
        if new_position._at_cell(col_to, row_to) in Figure.pawns() and abs(row_from - row_to) == 2:
            new_position._set_en_passant(row_to, col_to)
        else:
            new_position.en_passant = None
        if len(cell_to) == 3:
            # pawn transformation
            new_position.lines[row_to][col_to] = Figure(cell_to[2])
        return new_position

    def _move_figure(self, col_from: Column, row_from: int, col_to: Column, row_to: int) -> None:
        self.lines[row_to][col_to] = self.lines[row_from][col_from]
        self.lines[row_from][col_from] = None

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

    def get_cells_for_rook(self, col: Column, row: int) -> List[Tuple[Column, int]]:
        cells = []
        is_white = self._at_cell(col, row) in WHITES
        for c, to_right in ((col.left, False), (col.right, True)):
            while c:
                at_c = self._check_cell(c, row, is_white, cells)
                if at_c:
                    break
                c = c.right if to_right else c.left
        for r in (range(row + 1, 8), reversed(range(row))):
            for i in r:
                at_c = self._check_cell(col, i, is_white, cells)
                if at_c:
                    break
        return cells

    def get_cells_for_bishop(self, col: Column, row: int) -> List[Tuple[Column, int]]:
        cells = []
        is_white = self._at_cell(col, row) in WHITES
        for to_right in (False, True):
            c = col.right if to_right else col.left
            r = row + 1
            while c and r <= 7:
                at_c = self._check_cell(c, r, is_white, cells)
                if at_c:
                    break
                c = c.right if to_right else c.left
                r += 1
            r = row - 1
            c = col.right if to_right else col.left
            while c and r >= 0:
                at_c = self._check_cell(c, r, is_white, cells)
                if at_c:
                    break
                c = c.right if to_right else c.left
                r -= 1
        return cells

    def get_cells_for_queen(self, col: Column, row: int) -> List[Tuple[Column, int]]:
        return self.get_cells_for_rook(col, row) + self.get_cells_for_bishop(col, row)

    def _check_cell(self, col: Column, row: int, is_white: bool, cells: List[Tuple[Column, int]]) -> Optional[Figure]:
        at_c = self._at_cell(col, row)
        if not at_c or at_c in (WHITES if not is_white else BLACKS):
            cells.append((col, row))
        return at_c

    def get_cells_for_knight(self, col: Column, row: int) -> List[Tuple[Column, int]]:
        cells = []
        horizontal = [Column(col.value + 2) if col.value + 2 <= Column.h.value else None,
                      Column(col.value - 2) if col.value - 2 >= Column.a.value else None]
        for c in horizontal:
            if not c:
                continue
            if row < 7 and not self.lines[row + 1][c]:
                cells.append((c, row + 1))
            if row > 0 and not self.lines[row - 1][c]:
                cells.append((c, row - 1))
        vertical = [row - 2 if row >= 2 else None,
                    row + 2 if row <= 5 else None]
        for v in vertical:
            if v is None:
                continue
            if col != Column.h and not self.lines[v][col.right]:
                cells.append((col.right, v))
            if col != Column.a and not self.lines[v][col.left]:
                cells.append((col.left, v))
        return cells

    def __str__(self):
        output_lines = [BORDER_LINE]
        for j, line in zip(reversed(range(1, 9)), reversed(self.lines)):
            output_lines.append(f'{j} | {" ".join(s.value if s else "." for s in line.values())} |')
        output_lines.append(BORDER_LINE)
        output_lines.append(f'    {" ".join(Column.names())}  ')
        return '\n'.join(output_lines) + '\n\n'
