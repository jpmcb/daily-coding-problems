# Palindrome permutation

import unittest

def isPermPal(phrase):
    # build the table of chars (ignoring space and capitalization)
    # and populate it with the number of each char that appears
    table = {}
    length = 0
    for char in phrase:
        if(char != ' '):
            table[(char.lower())] = 0

    for char in phrase:
        if(char != ' '):
            length += 1
            table[(char.lower())] += 1

    isOdd = False if length % 2 == 0 else True

    for key in table:
        # Something is a permutation of a palindrome in several instances:
        # 1. If the number of chars (ignoring spaces) is even, then there must be an even number of each char
        # 2. If the num of chars is odd, there can be one (and only one) odd numbered char in the dict
        # 3. The isOdd flag tracks the odd / even factor of the palindrome
        if table[key] % 2 != 0 and isOdd == False and table[key] != ' ':
            return False
        if table[key] %2 != 0 and isOdd == True:
            isOdd = False
    
    return True

class Test(unittest.TestCase):
    dataT = [
        'taco cat',
        't acocat',
        'race car',
        'jhsabckuj ahjsbckj',
        'Able was I ere I saw Elba',
        'no x in nixon',
        'azAZ'
    ]

    dataF = [
        'This is not a pal',
        'abcddcbq',
        'So patient a nurse to nurse a patient so'
    ]

    def test_isPermPal(self):
        # true checks
        for data in self.dataT:
            result = isPermPal(data)
            self.assertTrue(result)

        for data in self.dataF:
            result = isPermPal(data)
            self.assertFalse(result)

if(__name__ == '__main__'):
    unittest.main()