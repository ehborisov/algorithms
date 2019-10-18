from chess_commons import Position
"""
1.Взятие на проходе

Дана FEN-позиция и ход пешкой.
Это может быть двойной прыжок пешки, 
в этом случае нужно установить признак "битового поля", если рядом есть пешка противника.
Это может быть взятие на проходе,
в этом случае нужно переместить нашу пешку и отдельно убрать пешку противника.

Необходимо выполнить ход и передать право хода.
Делать проверку на возможность хода не нужно.

Дано: 
   FEN-позиция
   ход фигурой
Надо:
   FEN-позиция после хода
"""


if __name__ == "__main__":
    tests_path = '/Users/eborisov/Downloads/2019-08-12_Chess-Tasks/3714.1.Взятие на проходе'
    for i in range(10):
        with open(f'{tests_path}/test.{i}.in') as input_file:
            test_input = input_file.read()
        with open(f'{tests_path}/test.{i}.out') as output_file:
            expected_out = output_file.read()
        fen_lines, move = test_input.strip().split('\n')
        position = Position(fen_lines)
        new_position = position.move(move[0:2], move[2:4])
        assert new_position.to_fen_string() == expected_out
