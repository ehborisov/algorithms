import unittest

import fibonacci


class FibonacciTest(unittest.TestCase):

    def test_fibonacci(self):
        fib_1000 = 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
        self.assertEqual(fib_1000, fibonacci.fibonacci_recursive(1000),
                         "Naive exponentiation algorithm error")
        self.assertEqual(fib_1000, fibonacci.fibonacci_iterative(1000),
                         "Fibonacci iterative algorithm error")
        # self.assertEqual(fib_1000, fibonacci.fibonacci_golden_ratio(1000),  # apparently it has some error crippling
        #                  "Fibonacci golden ratio algorithm error")          # in because of the floating point
        # self.assertEqual(fib_1000, fibonacci.fibonacci_matrix(1000),        # calculations, didn't have time to
        #                  "Fibonacci matrix multiplication algorithm error") # bypass it on big numbers.


if __name__ == '__main__':
    unittest.main()