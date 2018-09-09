# Check permutation:
# Given two strings, write a method to decide if one is a perm of the other

import unittest

def isPermutation(x, y):
    if(len(x) != len(y)):
        return False

    table = {}
    for char in x:
        table[char] = 0

    for char in x:
        table[char] += 1

    for char in y: 
        if char not in table:
            return False
        if table[char] == 0:
            return False
        table[char] -= 1

    return True 

class Test(unittest.TestCase):
    dataT = [
        ['abcd', 'dcba'],
        ['345543', '543345']
    ]
    dataF = [
        ['abcd', 'abce'],
        ['abcde', 'abc'],
        ['willywonka', 'willykonka']
    ]

    def test_isPermutation(self):
        # True checks
        for data in self.dataT:
            result = isPermutation(*data)
            self.assertTrue(result)

        for data in self.dataF:
            result = isPermutation(*data)
            self.assertFalse(result)

if(__name__ == '__main__'):
    unittest.main()