# Rotate Matrix

# Questions: Which direction is the matrix rotating?
# - Definition of an "image"?

import unittest

def rotate(matrix):

    n = len(matrix)
    for layer in range(n // 2):
        # layer variables
        first = layer
        last = n - layer - 1

        for i in range(first, last):
            offset = i - first
            saved = matrix[first][i]

            # Left -> Top
            matrix[first][i] = matrix[last - offset][first]

            # Bottom -> Left
            matrix[last - offset][first] = matrix[last][last - offset]

            # Right -> Bottom
            matrix[last][last - offset] = matrix[i][last]

            # Top -> Right
            matrix[i][last] = saved

    print(matrix)
    return matrix
    

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
        self.assertTrue(returned == self.data[1])
        

if(__name__ == '__main__'):
    unittest.main()