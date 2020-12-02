from .generalmatrix import Matrix


class SquareMatrix(Matrix):
    def __init__(self, matrix=None):
        Matrix.__init__(self, matrix)

    def __mul__(self, other):
        """ Function to multiply together two Matrices
        of size n-by-m
        
        Args:
            other (Matrix): Matrix instance
            
        Returns:
            Matrix: A different
            
        """
        n = int(self.get_dim().split('-')[0])
        m = int(self.get_dim().split('-')[2])
        q = int(other.get_dim().split('-')[0])
        p = int(other.get_dim().split('-')[2])
        result = [None for _ in range(n)]
        if m == q:
            for i in range(n):
                vals = []
                for j in range(p):
                    total = 0
                    for k in range(m):
                        total += self.matrix[i][k] * other.matrix[k][j]
                    vals.append(total)
                result[i] = vals
        else:
            result = None

        result = Matrix(result)
        return result
        
