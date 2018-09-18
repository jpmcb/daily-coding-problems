# Rotate Matrix

# Questions: Which direction is the matrix rotating?
# - Definition of an "image"?

import unittest

def swap(x, i, y, j):
    temp = x[i]
    x[i] = y[j]
    y[j] = temp

def rotate(matrix):

    n = len(matrix)
    for row in range(n // 2 + 1):
        for col in range(n):

            saved = None

            # Top
            saved = matrix[row][(col + 4)]
            swap(matrix)

            # Right

            # Bottom

            # Left
    

class Test(unittest.TestCase):
    data = [[
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ], [
        [21, 16, 11, 6, 1],
        [22, 17, 12, 7, 2],
        [23, 18, 13, 8, 3],
        [24, 19, 14, 9, 4],
        [25, 20, 15, 10, 5]
    ]]

    def testRotate(self):
        returned = rotate(self.data[0])
        self.assertTrue(returend == self.data[1])
        

if(__name__ == '__main__'):
    unittest.main()