import chess_commons
"""
1.FEN - ASCII

Дано расположение шахматных фигур на доске в FEN-нотации.

Вывести её в текстовом ASCII формате по образцу.
На диаграмме должно присутствовать:
рамка вокруг позиции, буквы a-h снизу, цифры 1-8 слева, точки на пустых полях, фигуры на своих местах

Начальные данные: строка символов - позиция в FEN нотации
Вывод результата: 11 строчек по 21 символу на каждом.

'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

  +-----------------+
8 | r n b q k b n r |
7 | p p p p p p p p |
6 | . . . . . . . . |
5 | . . . . . . . . |
4 | . . . . . . . . |
3 | . . . . . . . . |
2 | P P P P P P P P |
1 | R N B Q K B N R |
  +-----------------+
    a b c d e f g h   
"""


if __name__ == "__main__":
    tests_path = '/Users/eborisov/Downloads/2019-08-12_Chess-Tasks/1743.1.FEN - ASCII'
    for i in range(10):
        with open(f'{tests_path}/test.{i}.in') as input_file:
            test_input = input_file.read()
        with open(f'{tests_path}/test.{i}.out') as output_file:
            expected_out = output_file.read()
        out = chess_commons.represent_fen_string(test_input)
        assert out == expected_out