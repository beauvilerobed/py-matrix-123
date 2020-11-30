# python3


class Matrix:
    def __init__(self):
        """ A gerneral n-by-m matrix class for
        calculating basic algebra

            Attributes:
            n (int) the number of rows in the matrix
            m (int) the number of columns in the matrix
            with 0 < n * m < 2 ** 20

            matrix (list[list[floats]] the list of lists of floats

        """
        self._n = 0
        self._m = 0
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

    def add(self, nums):
        """ Function to add to the matrix attributes:

        Args:
            list[int] or list[list[int]]

        Returns:
            None
        """

        n = len(nums)
        try:
            m = len(nums[0])
        except TypeError:
            m = 1

        self._add_dim(n, m)
        self._add_matrix(nums)

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
            n, m = list(map(int, lines[0].split()))
            for line in lines[1:]:
                vals = list(map(float, line.split()))
                data_list.append(vals)

        f.close()

        if n == len(data_list) and m == len(data_list[0]):
            self._add_dim(n, m)
            self._add_matrix(data_list)
        else:
            print("file needs to be in correct format")

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

    def _add_matrix(self, nums):
        """ Private method util function to add a list of lists of values
        to the matrix class to obtain a matrix class

        Args:
            list[list[float]] or list[float]

        Returns:
            None

        """
        self._matrix = [None for i in range(self._n)]
        if self._m == 1:       
            for i in range(self._n):
                self._matrix[i] = [nums[i]]
        
        else:
            for i in range(self._n):
                self._matrix[i] = nums[i]
