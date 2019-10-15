from chess_commons import Position, Turn
"""
1.Счётчик ходов

Дана FEN-позиция и ход фигурой.
Нужно посчитать этот ход и передать право хода другой стороне.
ФИГУРЫ ПЕРЕМЕЩАТЬ НЕ НУЖНО

Дано: 
   FEN-позиция
   ход фигурой
Надо:
   FEN-позиция после хода
"""


if __name__ == "__main__":
    tests_path = '/Users/eborisov/Downloads/2019-08-12_Chess-Tasks/1746.1.Счётчик ходов'
    for i in range(5):
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
        assert position.to_fen_string() == expected_out
