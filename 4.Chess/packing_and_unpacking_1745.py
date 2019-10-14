from chess_commons import Position
"""
1.Сборка и разборка

Создать структуру для хранения позиции.
Написать функцию для парсинга FEN-позиции в эту структуру.
Написать функцию для формирования FEN-строки из этой структуры.

Дано: FEN-позиция, записанная с небольшими неточностями.
Надо: FEN-строка, созданная по данной позиции.
"""


if __name__ == "__main__":
    tests_path = '/Users/eborisov/Downloads/2019-08-12_Chess-Tasks/1745.1.Сборка и разборка'
    for i in range(10):
        with open(f'{tests_path}/test.{i}.in') as input_file:
            test_input = input_file.read()
        with open(f'{tests_path}/test.{i}.out') as output_file:
            expected_out = output_file.read()
        position = Position(test_input)
        out = position.to_fen_string()
        assert out == expected_out

