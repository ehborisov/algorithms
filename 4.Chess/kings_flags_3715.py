from chess_commons import Position
"""
1.Королевские флаги

Дана FEN-позиция и ход.
Это может быть любой ход, кроме рокировки.
Если это ход ладьёй - необходимо убрать флаг рокировки для этого игрока в сторону этой ладьи.
Если это ход королём - необходимо убрать флаг рокировки для этого игрока.
Если это взятие ладьи - необходимо убрать флаг рокировки для взятой ладьи.

Необходимо выполнить ход и передать право хода.
Делать проверку на возможность хода не нужно.

Дано: 
   FEN-позиция
   ход фигурой
Надо:
   FEN-позиция после хода
"""


if __name__ == "__main__":
    tests_path = '/Users/eborisov/Downloads/2019-08-12_Chess-Tasks/3715.1.Королевские флаги'
    for i in range(10):
        with open(f'{tests_path}/test.{i}.in') as input_file:
            test_input = input_file.read()
        with open(f'{tests_path}/test.{i}.out') as output_file:
            expected_out = output_file.read()
        fen_lines, move = test_input.strip().split('\n')
        position = Position(fen_lines)
        new_position = position.move(move[0:2], move[2:])
        assert new_position.to_fen_string() == expected_out
