import unittest
from pymatrix import Matrix, SquareMatrix


class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix()
        self.matrix.read_data_file('numbers-1-by-4.txt')
        self.nullcase = ([[1] * 2 ** 10 for _ in range(2 ** 10)],
                         [[1] * 2 ** 7 for _ in range(2 ** 13)], [])

    def test_read_data(self):
        self.assertEqual(self.matrix.get_dim(), "1-by-4")
        self.matrix.read_data_file('numbers-4-by-1.txt')
        self.assertEqual(self.matrix.get_dim(), "4-by-1")
    
    def test_add(self):
        cases = [
            ([1, 3, 4, 5], [[1], [3], [4], [5]]),
            ([[1], [3], [4], [5]], [[1], [3], [4], [5]]),
            ([[1, 3, 4, 5]], [[1, 3, 4, 5]]),
            ([[1, 2, -3], [0, -1.0, 3.9], [0, -1.0, 3.9], [0, -1.0, 3.9]], 
             [[1, 2, -3], [0, -1.0, 3.9], [0, -1.0, 3.9], [0, -1.0, 3.9]]),
        ]

        for case, solution in cases:
            self.matrix.add(case)
            self.assertEqual(self.matrix.matrix, solution)

    def test_get_dim_small(self):
        cases = [
            ([1, 3, 4, 5], "4-by-1"),
            ([[1], [3], [4], [5]], "4-by-1"),
            ([[1, 3, 4, 5]], "1-by-4"),
            ([[1, 2, -3], 
              [0, -1.0, 3.9], 
              [0, -1.0, 3.9], 
              [0, -1.0, 3.9]], "4-by-3"),
        ]

        for case, solution in cases:
            self.matrix.add(case)
            self.assertEqual(self.matrix.get_dim(), solution)

    def test_get_dim_large(self):
        cases = [
            ([1] * 2 ** 20, "1048576-by-1"),
            ([[1] * 2 ** 10 for _ in range(2 ** 10)], "1024-by-1024"),
            ([[1] * 2 ** 7 for _ in range(2 ** 13)], "8192-by-128"),
        ]

        for case, solution in cases:
            self.matrix.add(case)
            self.assertEqual(self.matrix.get_dim(), solution)
    
    def test_add_two_matrices_small(self):
        cases = [
            ([[1], [3], [4], [5]], 
             [[1], [0], [2], [5]], 
             [[1+1], [3+0], [4+2], [5+5]]),

            ([[1, 2], [3, -1], [4, 0.0], [5, -18]], 
             [1, 0, 2, 5], []),

            ([1.1, 3, 4, 5], 
             [1, 0, -2.0, -5], 
             [[1.1+1], [3+0], [4-2.0], [5-5]])
        ]
        for A, B, solution in cases:
            matrixA = Matrix(A)
            matrixB = Matrix(B)
            matrixSol = Matrix(solution)
            matrixActual = matrixA + matrixB
            self.assertEqual(matrixActual.matrix, matrixSol.matrix)

    def test_add_two_matrices_large(self):
        cases = [
            ([1] * 2 ** 18, [1] * 2 ** 18, [[1+1]] * 2 ** 18),
            ([[1, 2, 3]] * 2 ** 15, 
             [[1, 2, 3]] * 2 ** 15, 
             [[1+1, 2+2, 3+3]] * 2 ** 15),
            self.nullcase,
        ]
        for A, B, solution in cases:
            matrixA = Matrix(A)
            matrixB = Matrix(B)
            matrixSol = Matrix(solution)
            matrixActual = matrixA + matrixB
            self.assertEqual(matrixActual.matrix, matrixSol.matrix)
    
    def test_subtract_two_matrices_small(self):
        cases = [
            ([[1], [3], [4], [5]], 
             [[1], [0], [2], [5]], 
             [[1-1], [3-0], [4-2], [5-5]]),

            ([[1, 2], [3, -1], [4, 0.0], [5, -18]], 
             [1, 0, 2, 5], []),

            ([1.1, 3, 4, 5], 
             [1, 0, -2.0, -5], 
             [[1.1-1], [3-0], [4-(-2.0)], [5-(-5)]])
        ]
        for A, B, solution in cases:
            matrixA = Matrix(A)
            matrixB = Matrix(B)
            matrixSol = Matrix(solution)
            matrixActual = matrixA - matrixB
            self.assertEqual(matrixActual.matrix, matrixSol.matrix)

    def test_subract_two_matrices_large(self):
        cases = [
            ([1] * 2 ** 18, [1] * 2 ** 18, [[1-1]] * 2 ** 18),
            ([[1, 2, 3]] * 2 ** 15, 
             [[1, 2, 3]] * 2 ** 15, 
             [[1-1, 2-2, 3-3]] * 2 ** 15), self.nullcase,
        ]
        for A, B, solution in cases:
            matrixA = Matrix(A)
            matrixB = Matrix(B)
            matrixSol = Matrix(solution)
            matrixActual = matrixA - matrixB
            self.assertEqual(matrixActual.matrix, matrixSol.matrix)
    
    def test_scalar_mul(self):
        cases = [
            (5.0, [[1], [0], [2], [5]], 
                  [[5.0*1], [5.0*0], [2*5.0], [5*5.0]]),

            (3, [1, 0, 2, 5], 
                [3*1, 3*0, 2*3, 3*5]),

            (0, [[2.1, 9], [3, 3], [2.0, 5], [0, 7]], 
                [[2.1*0, 9*0], [3*0, 0*0], [0*2.0, 0*0], [0*0, 7*0]])
        ]
        for num, A, solution in cases:
            matrixA = Matrix(A)
            actual = matrixA * num
            matrixSol = Matrix(solution)
            self.assertEqual(actual.matrix, matrixSol.matrix)

    def test_scalar_mul_large(self):
        cases = [
            (18.1, [1] * 2 ** 18, [[1*18.1]] * 2 ** 18),
            (-15, [[1, 2, 3]] * 2 ** 15, [[-15*1, -15*2, -15*3]] * 2 ** 15),
        ]
        for num, A, solution in cases:
            matrixA = Matrix(A)
            actual = matrixA * num
            matrixSol = Matrix(solution)
            self.assertEqual(actual.matrix, matrixSol.matrix)


class TestSquareMatrix(unittest.TestCase):
    def setUp(self):
        self.nullcase = ([[1] * 2 ** 10 for _ in range(2 ** 10)],
                         [[1] * 2 ** 7 for _ in range(2 ** 13)], [])

    def test_matrix_multiply_small(self):
        cases = [
            ([[1, 2], [3, 4]], 
             [[4, 3], [2, 1]], 
             [[1*4 + 2*2, 1*3 + 2*1], [3*4 + 4*2, 4*1+3*3]]),

            ([[1, 2, 0], 
              [3, 4, -1.0], 
              [2, 4, 0]], 

             [[4, 3, -1], 
              [2, 1, 2.0], 
              [0, 15, -1.1]], 

             [[1*4+2*2+0*0, 1*3+2*1+0*15, 1*(-1)+2*2.0+0*(-1.1)], 
              [3*4+4*2+(-1.0)*0, 4*1+3*3+(-1.0)*15, 3*(-1)+4*2.0+(-1.0)*(-1.1)], 
              [2*4+4*2+0*0, 2*3+4*1+0*15, 2*(-1)+(2.0)*4+0*(-1.1)]]),
        ]
        for A, B, solution in cases:
            matrixA = SquareMatrix(A)
            matrixB = SquareMatrix(B)
            actual = matrixA * matrixB
            matrixSol = SquareMatrix(solution)
            self.assertEqual(actual.matrix, matrixSol.matrix)


if __name__ == '__main__':
    unittest.main()
