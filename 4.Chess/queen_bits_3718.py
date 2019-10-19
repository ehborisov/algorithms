from chess_commons import Position, get_cell_for_number, get_cell_number, set_bit, Figure

"""
2.Ферзь - BITS *

Дана шахматная позиция в FEN формате.
Известно, что в этой позиции есть:
одна белая ладья,
один белый слон,
один белый ферзь,
а также возможно наличие других белых и чёрных фигур.
Определить битовую маску возможных ходов белых фигур - ладьи, слона и ферзя.
Ладья ходит по вертикалям и горизонталям.
Слон ходит по диагоналям.
Ферзь ходит как ладья и слон вместе.
Фигура обязана пойти как минимум на одну клетку.
Фигура не может перепрыгивать другие фигуры.
Фигура может пойти на пустую клетку или
на клетку с фигурой противоположного цвета.

Начальные данные: строка с шахматной позицией в FEN-формате.
Вывод результата: 3 числа типа ulong на трёх строчках.
на первой строке - число, соответствующее битовой маске возможных ходов белой ладьи
на второй строке - число, соответствующее битовой маске возможных ходов белого слона
на третьей строке - число, соответствующее битовой маске возможных ходов белого ферзя
"""


if __name__ == "__main__":
    tests_path = '/Users/eborisov/Downloads/2019-08-12_Chess-Tasks/3718.2.Ферзь - BITS _'
    for i in range(10):
        with open(f'{tests_path}/test.{i}.in') as input_file:
            test_input = input_file.read()
        with open(f'{tests_path}/test.{i}.out') as output_file:
            expected_out = output_file.read()
        position = Position(test_input.strip(), with_end=False)
        queen_cell = None
        rook_cell = None
        bishop_cell = None
        for j, row in enumerate(position.lines):
            for col, figure in row.items():
                if figure == Figure.W_QUEEN:
                    queen_cell = (col, j)
                elif figure == Figure.W_BISHOP:
                    bishop_cell = (col, j)
                elif figure == Figure.W_ROOK:
                    rook_cell = (col, j)
        rook_cells = position.get_cells_for_rook(*rook_cell)
        bishop_cells = position.get_cells_for_bishop(*bishop_cell)
        queen_cells = position.get_cells_for_queen(*queen_cell)
        rook, bishop, queen = 0, 0, 0
        for cell in rook_cells:
            rook = set_bit(rook, get_cell_number(*cell))
        for cell in bishop_cells:
            bishop = set_bit(bishop, get_cell_number(*cell))
        for cell in queen_cells:
            queen = set_bit(queen, get_cell_number(*cell))
        assert f"{rook}\n{bishop}\n{queen}\n" == expected_out

