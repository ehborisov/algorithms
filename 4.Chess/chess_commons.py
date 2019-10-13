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


BORDER_LINE = '  +-----------------+'


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


def represent_fen_string(fen_string, with_end=True):
    lines = split_fen_string(fen_string, with_end)[0]
    output_lines = [BORDER_LINE]
    for j, line in zip(reversed(range(1, 9)), lines):
        out_line = ''
        for s in line:
            out_line += '.' * int(s) if s.isdigit() else s
        output_lines.append(f'{j} | {" ".join(out_line)} |')
    output_lines.append(BORDER_LINE)
    output_lines.append(f'    {" ".join("abcdefgh")}  ')
    return '\n'.join(output_lines) + '\n\n'
