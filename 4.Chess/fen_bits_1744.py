import chess_commons

"""
1.FEN - BITS *

Дано расположение шахматных фигур на доске в FEN-нотации.
(дана только первая часть fen-кода)

Например, начальная позиция записывается так: rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR

Перевести её в Bitboard Board-Definition формат.

в 64-битном числе хранятся биты каждой клетки шахматной доски:
поле a1 соответствует нулевому биту и равно 0 = 1
поле b1 соответствует первому  биту и равно 1 = 2
поле h1 соответствует седьмому биту и равно 7 = 128
поле a2 соответствует восьмому биту и равно 8 = 256.
поле h8 соответствует 63-ему биту и равно 63 = 9 223 372 036 854 775 808.

Для хранения позиции использовать массив board 64-битных беззнаковых целых чисел: ulong [12] board

Каждый элемент массива board хранит битовую маску фигур (0-нет, 1-есть) в порядке перечисления Piece:

enum Piece
{
   whitePawns,
   whiteKnights,
   whiteBishops,
   whiteRooks,
   whiteQueens,
   whiteKing,
 
   blackPawns,
   blackKnights,
   blackBishops,
   blackRooks,
   blackQueens,
   blackKing
}

Начальные данные: строка символов - позиция в FEN нотации
Вывод результата: 12 беззнаковых 64-битных целых чисел, по одному на каждой строке.

Комментарий к демо-тесту:
первая строчка - битбоард для расположения белых пешек - поля a2 b2 ... h2
 - равно 28 + 29 + ... + 215 = 256 + 512 + ... + 32768 = 65280.
вторая строчка - битбоард для расположения белых коней - поля b1 g1 - равно 21 + 26 = 2 + 64 = 66.
третья строчка - битбоард для расположения белых слонов - поля c1 f1 - равно 22 + 25 = 4 + 32 = 36.
четвёртая строчка - битбоард для расположения белых ладей - поля a1 h1 - равно 20 + 27 = 1 + 128 = 129.
пятая строчка - битбоард для расположения белых ферзей - поле d1 - равно 23 = 8.
шестая строчка - битбоард для расположения белого короля - поле e1 - равно 24 = 16.
"""


def convert_fen_to_bits(fen_input):
    board = [0] * 12
    figures_mapping = {
        chess_commons.Figure.W_PAWN: 0,
        chess_commons.Figure.W_KNIGHT: 1,
        chess_commons.Figure.W_BISHOP: 2,
        chess_commons.Figure.W_ROOK: 3,
        chess_commons.Figure.W_QUEEN: 4,
        chess_commons.Figure.W_KING: 5,
        chess_commons.Figure.B_PAWN: 6,
        chess_commons.Figure.B_KNIGHT: 7,
        chess_commons.Figure.B_BISHOP: 8,
        chess_commons.Figure.B_ROOK: 9,
        chess_commons.Figure.B_QUEEN: 10,
        chess_commons.Figure.B_KING: 11,
    }
    lines = fen_input.split('/')
    for j, line in enumerate(reversed(lines)):
        position_in_line = 0
        for c in line:
            if c.isdigit():
                position_in_line += int(c)
            else:
                figure_index = figures_mapping[chess_commons.Figure(c)]
                board[figure_index] = chess_commons.set_bit(board[figure_index], 8 * j + position_in_line)
                position_in_line += 1
    return '\n'.join(str(s) for s in board) + '\n'


if __name__ == "__main__":
    tests_path = '/Users/eborisov/Downloads/2019-08-12_Chess-Tasks/1744.1.FEN - BITS _'
    for i in range(10):
        with open(f'{tests_path}/test.{i}.in') as input_file:
            test_input = input_file.read()
        with open(f'{tests_path}/test.{i}.out') as output_file:
            expected_out = output_file.read()
        out = convert_fen_to_bits(test_input.strip())
        assert out == expected_out
