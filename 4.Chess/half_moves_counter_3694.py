from chess_commons import Position, Turn, Figure
"""
1.Счётчик полуходов

Дана FEN-позиция и ход фигурой.
Нужно посчитать этот ход, передать право хода другой стороне,
а также увеличить или сбросить счётчик полуходов для правила 50 ходов.
Счётчик сбрасывается, если было взятие или ход пешкой.
В остальных случаях счётчик увеличивается на 1 после каждого полухода.
ФИГУРЫ ПЕРЕМЕЩАТЬ НЕ НУЖНО

Дано: 
   FEN-позиция
   ход фигурой
Надо:
   FEN-позиция после хода
"""


if __name__ == "__main__":
    tests_path = '/Users/eborisov/Downloads/2019-08-12_Chess-Tasks/3694.1.Счётчик полуходов'
    for i in range(10):
        with open(f'{tests_path}/test.{i}.in') as input_file:
            test_input = input_file.read()
        with open(f'{tests_path}/test.{i}.out') as output_file:
            expected_out = output_file.read()
        fen_lines, move = test_input.strip().split('\n')
        position = Position(fen_lines)
        if position.turn == Turn.BLACKS:
            position.full_moves += 1
            position.turn = Turn.WHITES
        else:
            position.turn = Turn.BLACKS
        position.half_moves += 1
        mv_from, mv_to = move[0:2], move[2:4]
        capture = position.at_cell(mv_to) in list(Figure)
        pawn_move = position.at_cell(mv_from) in [Figure.B_PAWN, Figure.W_PAWN]
        if pawn_move or capture:
            position.half_moves = 0
        assert position.to_fen_string() == expected_out

