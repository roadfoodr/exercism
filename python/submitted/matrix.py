import numpy as np

class Matrix(object):
    """
    Class that converts a string representing a 2-D matrix of ints (elements
    separated by whitespace, rows separated by '\n'), into an object that can
    be queried by (one-based) index for an individual row or column.
    """
    def __init__(self, matrix_string):
        self.num_rows = matrix_string.count('\n') + 1
        self.matrix = np.fromstring(matrix_string, dtype=int, sep=' ').reshape(
                (self.num_rows, -1))
        self.num_cols = self.matrix.shape[1]
        return

    def row(self, index):
        if index < 1:
            raise ValueError("index must be at least 1")
        if index > self.num_rows:
            raise ValueError("index is greater than the number of rows")
        return self.matrix[index - 1, :].tolist()

    def column(self, index):
        if index < 1:
            raise ValueError("index must be at least 1")
        if index > self.num_cols:
            raise ValueError("index is greater than the number of columns")
        return self.matrix[:, index - 1].tolist()
