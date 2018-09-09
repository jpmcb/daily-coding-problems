# Palindrome permutation

import unittest

def isPermPal(phrase):
    # build the table
    table = {}
    for char in phrase:
        table[char] = 0

    for char in phrase:
        table[char] += 1

    # Check if it's a palandrome
    if(len(string) % 2 == 0):
        isOdd = False
    for key in table:
        if table[key] % 2 != 0 and isOdd != True and table[key] != ' ':
            return False
        if table[key] %2 != 0 and isOdd != False:
            isOdd = False
    
    return True

class Test(unittest.TestCase):
    dataT[
        ['taco']
    ]