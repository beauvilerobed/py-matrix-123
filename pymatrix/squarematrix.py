from .generalmatrix import Matrix


class SquareMatrix(Matrix):
    def __init__(self, matrix=None):
        Matrix.__init__(self, matrix)

    def __mul__(self, other):
        """ Function to multiply together two Matrices
        of square size
        
        Args:
            other (Matrix): Matrix instance
            
        Returns:
            Matrix: A different
            
        """
        def strassen(x, y, n):
            x = x.matrix
            y = y.matrix

            # base case: 1x1 matrix
            if n == 1:
                z = [[0]]
                z[0][0] = x[0][0] * y[0][0]
                return z
            else:
                # split matrices into quarters
                a, b, c, d = split(x)
                e, f, g, h = split(y)

                a = SquareMatrix(a)
                b = SquareMatrix(b)
                c = SquareMatrix(c)
                d = SquareMatrix(d)
                e = SquareMatrix(e)
                f = SquareMatrix(f)
                g = SquareMatrix(g)
                h = SquareMatrix(h)

                # p1 = a*(f-h)
                p1 = SquareMatrix(strassen(a, f-h, n/2))

                # p2 = (a+b)*h
                p2 = SquareMatrix(strassen(a+b, h, n/2))

                # p3 = (c+d)*e
                p3 = SquareMatrix(strassen(c+d, e, n/2))

                # p4 = d*(g-e)
                p4 = SquareMatrix(strassen(d, g-e, n/2))

                # p5 = (a+d)*(e+h)
                p5 = SquareMatrix(strassen(a+d, e+h, n/2))

                # p6 = (b-d)*(g+h)
                p6 = SquareMatrix(strassen(b-d, g+h, n/2))

                # p7 = (a-c)*(e+f)
                p7 = SquareMatrix(strassen(a-c, e+f, n/2))

                z11 = (((p5 + p4) - p2) + p6).matrix

                z12 = (p1 + p2).matrix

                z21 = (p3 + p4).matrix

                z22 = (((p5 - p3) - p7) + p1).matrix

                r, c = len(z11)*2, len(z11)*2
                z = [[0 for _ in range(r)] for _ in range(c)]
                for i in range(len(z11)):
                    for j in range(len(z11)):
                        z[i][j] = z11[i][j]
                        z[i][j+len(z11)] = z12[i][j]
                        z[i+len(z11)][j] = z21[i][j]
                        z[i+len(z11)][j+len(z11)] = z22[i][j]
                
                return z
            
        def split(matrix):
            """Split matrix into quarters."""
            a = b = c = d = matrix

            while len(a) > len(matrix)/2:
                a = a[:len(a)//2]
                b = b[:len(b)//2]
                c = c[len(c)//2:]
                d = d[len(d)//2:]
            while len(a[0]) > len(matrix[0])//2:
                for i in range(len(a[0])//2):
                    a[i] = a[i][:len(a[i])//2]
                    b[i] = b[i][len(b[i])//2:]
                    c[i] = c[i][:len(c[i])//2]
                    d[i] = d[i][len(d[i])//2:]
            return a, b, c, d

        dim1 = self.get_dim().split('-')[2]
        dim2 = self.get_dim().split('-')[0]
        if dim1 == dim2:
            new = SquareMatrix(strassen(self, other, int(dim1)))
        else:
            new = SquareMatrix()
        return new
