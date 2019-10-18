from chess_commons import Position
"""
1.Рокировка

Дана FEN-позиция и ход королём на две клетки влево или вправо - 
это длинная или короткая рокировка, соответственно.
Король может сделать и другой ход, на одну клетку,
в этом случае ладью перемещать не нужно.

Необходимо переставить короля и ладью.

Необходимо выполнить ход и передать право хода.
Делать проверку на возможность хода не нужно.

Дано: 
   FEN-позиция
   ход фигурой
Надо:
   FEN-позиция после хода
"""


if __name__ == "__main__":
    tests_path = '/Users/eborisov/Downloads/2019-08-12_Chess-Tasks/3716.1.Рокировка'
    for i in range(5):
        with open(f'{tests_path}/test.{i}.in') as input_file:
            test_input = input_file.read()
        with open(f'{tests_path}/test.{i}.out') as output_file:
            expected_out = output_file.read()
        fen_lines, move = test_input.strip().split('\n')
        position = Position(fen_lines)
        new_position = position.move(move[0:2], move[2:])
        assert new_position.to_fen_string() == expected_out
