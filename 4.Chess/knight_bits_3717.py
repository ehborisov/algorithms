from chess_commons import Position, set_bit, get_cell_for_number, get_cell_number, EMPTY_BOARD_FEN

"""
2.Конь - BITS *

Шахматный конь решил пробежаться по шахматной доске.
Сейчас он находится в указанной клетке.
Куда он может сейчас походить?
Вывести количество возможных ходов коня
и ulong число с установленными битами тех полей, куда он может походить.

Начальные данные: число от 0 до 63 - индекс позиции коня
Клетки нумеруются от а1 = 0, b1 = 1 до h8 = 63.

Вывод результата: два числа на двух клетках,
количество возможных ходов
битовая маска всех возможных ходов коня.

На доске кроме коня никого нет, конь ходит буквой "Г" (две клетки вперёд и 1 вбок).

http://www.talkchess.com/forum3/viewtopic.php?t=39053
"""


if __name__ == "__main__":
    tests_path = '/Users/eborisov/Downloads/2019-08-12_Chess-Tasks/3717.2.Конь - BITS _'
    for i in range(10):
        print(f"case {i}")
        with open(f'{tests_path}/test.{i}.in') as input_file:
            test_input = input_file.read()
        with open(f'{tests_path}/test.{i}.out') as output_file:
            expected_out = output_file.read()
        knight_cell = get_cell_for_number(int(test_input))
        position = Position(EMPTY_BOARD_FEN)
        allowed_cells = position.get_cells_for_knight(*knight_cell)
        result = 0
        for cell in allowed_cells:
            result = set_bit(result, get_cell_number(*cell))
        assert f"{len(allowed_cells)}\n{result}\n" == expected_out
