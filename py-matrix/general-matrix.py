# python3


class Matrix:
    def __init__(self):
        """ A gerneral n-by-m matrix class for
        calculating basic algebra

            Attributes:
            n (int) the number of rows in the matrix
            m (int) the number of columns in the matrix
            matrix (list[list[floats]] the list of lists of floats

        """
        self._n = None
        self._m = None
        self._matrix = list()

    def get_dim(self):
        """ A method to return the dimension of
        the matrix class

        Args: None

        Return:
            dimension of the matrix
            e.g. A = 0 1 2
                     3 2 5
                     0 1 1
                     7 6 5

            So should return 4-by-3

        """
        return "{}-by-{}".format(self._n, self._m)

    def add(self, vals_of_vals):
        """ Function to add to the matrix attributes:

        Args:
            list[int] or list[list[int]]

        Returns:
            None
        """

        n = len(vals_of_vals)
        try:
            m = len(vals_of_vals[0])
        except TypeError:
            m = 1

        self._add_dim(n, m)
        self._add_matrix(vals_of_vals)

    def read_data_file(self, file_name):
        """ Method in Matrix class to read in data from a txt file. The txt file
        should have 2 numbers (the number of rows value and the number
        of columns) in the first line. The next lines should be an equal number
        of values (floats).

        The numbers are stored in the data attributes
        e.g.
        txt file should look like this

        2 3
        1 2 5.0
        6 -1 0

        Args:
            file_name (string): name of a file to read from

        Returns:
            None

        """
        with open(file_name) as f:
            data_list = []
            lines = f.readlines()
            n, m = list(map(float, lines[0].split()))
            for line in lines[1:]:
                vals = list(map(float, line.split()))
                data_list.append(vals)

        if n == len(data_list) and m == len(data_list[0]):
            self._add_dim(n, m)
            self._add_matrix(data_list)
        else:
            print("file need to be in correct format")

    def _add_dim(self, n, m):
        """ Private method util function to add dimension to the rectangular matrix

        Args:
            n (int) number of rows
            m (int) numbers of columns

        Returns:
            None

        """
        self._n = n
        self._m = m

    def _add_matrix(self, vals_of_vals):
        """ Private method util function to add a list of lists of values
        to the matrix class to obtain a matrix class

        Args:
            list[list[float]]

        Returns:
            None

        """

        for i in range(self._n):
            self._matrix[i] = []
            for j in range(self._m):
                val_index = vals_of_vals[i][j]
                self._matrix[i].append(val_index)
