from enum import Enum
from typing import Optional
from itertools import groupby


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


COLUMN_CHARACTERS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
EMPTY_SQUARE = '.'


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
    output_lines.append(f'    {" ".join(COLUMN_CHARACTERS)}  ')
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
        self.en_passant = tuple(s for s in en_passant) if en_passant != EMPTY_DATA else None
        self.half_moves = int(half_moves)
        self.full_moves = int(full_moves)
        self.lines = Position._convert_raw_lines(raw_lines)

    @classmethod
    def _convert_raw_lines(cls, raw_lines):
        lines = []
        for line in raw_lines:
            if not line:
                lines.append({c: None for c in COLUMN_CHARACTERS})
                continue
            converted_line = {}
            position_pointer = 0
            for s in line:
                if s.isdigit():
                    for c in COLUMN_CHARACTERS[position_pointer: position_pointer+int(s)]:
                        converted_line[c] = None
                    position_pointer += int(s)
                else:
                    converted_line[COLUMN_CHARACTERS[position_pointer]] = Figure(s)
                    position_pointer += 1
            if position_pointer != 8:
                for c in COLUMN_CHARACTERS[position_pointer: 8]:
                    converted_line[c] = None
            lines.append(converted_line)
        return lines

    def get_position(self, col: str, row: int) -> Optional[Figure]:
        return self.lines[row][col]

    def to_fen_string(self):
        fen_lines = []
        for line in self.lines:
            # that could have been more readable but I was too keen to use one-liners in the recreational coding
            # in effect, itertools.groupby just gives an item:iterator[over same items in a row] for item in a sequence
            fen_lines.append(''.join(''.join(e.value for e in elements) if key else str(len(list(elements)))
                                     for key, elements in groupby(line.values())))
        castling_data = (''.join(sorted(k.value if v else '' for k, v in self.castling_map.items()))
                         if any(self.castling_map.values()) else EMPTY_DATA)
        en_passant = ''.join(self.en_passant) if self.en_passant else EMPTY_DATA
        return f"{'/'.join(fen_lines)} {self.turn.value} {castling_data} {en_passant} {self.half_moves}" \
               f" {self.full_moves}\n"

    def __str__(self):
        output_lines = [BORDER_LINE]
        for j, line in zip(reversed(range(1, 9)), self.lines):
            output_lines.append(f'{j} | {" ".join(s.value if s else "." for s in line.values())} |')
        output_lines.append(BORDER_LINE)
        output_lines.append(f'    {" ".join(COLUMN_CHARACTERS)}  ')
        return '\n'.join(output_lines) + '\n\n'
