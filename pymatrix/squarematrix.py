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
        m = int(self.get_dim().split('-')[2])
        q = int(other.get_dim().split('-')[0])
        result = [None for _ in range(m)]
        if m == q:
            for i in range(m):
                vals = []
                for j in range(m):
                    total = 0
                    for k in range(m):
                        total += self.matrix[i][k] * other.matrix[k][j]
                    vals.append(total)
                result[i] = vals
        else:
            result = None

        result = Matrix(result)
        return result
        
    def trace(self):
        """ Function to take the trace of a Matrices
        of size n-by-n

        n (int) number of rows and column

        Args:
            other (Matrix): Matrix instance
            
        Returns:
            float
            
        """
        trace = 0
        n = int(self.get_dim().split('-')[0])
        for i in range(n):
            trace += self.matrix[i][i]

        return trace
        