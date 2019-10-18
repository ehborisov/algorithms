from chess_commons import Position
"""
1.Превращение пешки

Дана FEN-позиция и ход пешкой с превращением.
Фигура превращения записывается сразу после координат.
Необходимо выполнить превращение и передать право хода.
Делать проверку на возможность хода не нужно.

Дано:
   FEN-позиция
   ход фигурой
Надо:
   FEN-позиция после хода
"""


if __name__ == "__main__":
    tests_path = '/Users/eborisov/Downloads/2019-08-12_Chess-Tasks/3713.1.Превращение пешки'
    for i in range(10):
        with open(f'{tests_path}/test.{i}.in') as input_file:
            test_input = input_file.read()
        with open(f'{tests_path}/test.{i}.out') as output_file:
            expected_out = output_file.read()
        fen_lines, move = test_input.strip().split('\n')
        position = Position(fen_lines)
        new_position = position.move(move[0:2], move[2:5])
        assert new_position.to_fen_string() == expected_out
