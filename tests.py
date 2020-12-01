import unittest
from pymatrix import Matrix



class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix()
        self.matrix.read_data_file('numbers-1-by-4.txt')

    def test_read_data(self):
        self.assertEqual(self.matrix.get_dim(), "1-by-4")
        self.matrix.read_data_file('numbers-4-by-1.txt')
        self.assertEqual(self.matrix.get_dim(), "4-by-1")

    def test_get_dim_small(self):
        cases = [
            ([1, 3, 4, 5], "4-by-1"),
            ([[1], [3], [4], [5]], "4-by-1"),
            ([[1, 3, 4, 5]], "1-by-4"),
            ([[1, 2, -3], [0, -1.0, 3.9], [0, -1.0, 3.9], [0, -1.0, 3.9]], "4-by-3"),
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
             [[2.0], [3.0], [6.0], [10.0]]),

            ([[1, 2], [3, -1], [4, 0.0], [5, -18]], 
             [1, 0, 2, 5], 
              None),

            ([1.1, 3, 4, 5], 
             [1, 0, -2.0, -5], 
             [[2.0, 2.0, 4.0, 0.0]])
        ]
        for A, B, solution in cases:
            matrixA = Matrix()
            matrixA.add(A)
            matrixB = Matrix()
            matrixB.add(B)
            if solution is not None:
                matrixSol = Matrix()
                matrixSol.add(solution)
            else:
                matrixSol = None
            self.assertEqual(matrixA + matrixB, matrixSol)

    def test_add_two_matrices_large(self):
        cases = [
            ([1] * 2 ** 20, [1] * 2 ** 20, [2.0] * 2 ** 20),
            ([[1] * 2 ** 10 for _ in range(2 ** 10)],
             [[1] * 2 ** 7 for _ in range(2 ** 13)], 
             None),
        ]
        for A, B, solution in cases:
            matrixA = Matrix()
            matrixA.add(A)
            matrixB = Matrix()
            matrixB.add(B)
            if solution is not None:
                matrixSol = Matrix()
                matrixSol.add(solution)
            else:
                matrixSol = None
            self.assertEqual(matrixA + matrixB, matrixSol)


if __name__ == '__main__':
    unittest.main()
