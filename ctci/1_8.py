# Zero Matrix

import unittest

# -------------------------------
# Makes a column in a matrix zero

def make_col_zero(matrix, col):
    for row in matrix:
        row[col] = 0

# -------------------------------
# Makes a row in a matrix zero

def make_row_zero(matrix, row):
    for i in range(len(matrix[row])):
        matrix[row][i] = 0

def zero_matrix(matrix):
    # Check first if the first col / row are zero
    rowZero = False
    colZero = False

    for num in matrix[0]:
        if num == 0: rowZero = True

    for i in range(len(matrix)):
        if matrix[i][0] == 0: colZero = True

    # Go through the matrix and set the matrix first row / col to zero
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            if(matrix[i][j] == 0):
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Go through the first column and set the flagged columns 
    for col in range(len(matrix[0])):
        if matrix[0][col] == 0:
            make_col_zero(matrix, col)

    # Go through the first row and set the flagged rows
    for row in range(len(matrix)):
        if matrix[row][0] == 0:
            make_row_zero(matrix, row)

    # Reset the first row and first col if needed
    if rowZero: make_row_zero(matrix, 0)
    if colZero: make_col_zero(matrix, 0)

    return matrix

class Test(unittest.TestCase):

    data = [[
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1],
        ],[
            [1, 1, 1, 0, 1],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1],
        ],[
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
]
    ]

    def test_zero(self):
        returned = zero_matrix(self.data[0])
        self.assertTrue(returned == self.data[1])
        returned = zero_matrix(self.data[2])
        self.assertTrue(returned == self.data[3])

if __name__ == "__main__":
    unittest.main()