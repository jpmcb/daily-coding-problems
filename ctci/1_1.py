# Is Unique:
# Implement an algorithm to determine if a string has all unique characters. What if you cannot utilize additional data structures?

import unittest

def isUnique(input):
    # Assuming ascii 128 settup
    if (len(input) > 128):
        return False
    else:
        charSet = {}
        for x in input:
            if (x in charSet):
                return False
            else:
                charSet[x] = True
        
        return True

class Test(unittest.TestCase):
    dataT = [('abcd'), ('abcdefghijklmnopqrstuvwxyz'), ('q5irt'), ('')]
    dataF = [('23abc32'), ('hb 7jd8 h()')]

    def test_isUnique(self):
        # true checks
        print("Running true string checks")
        for true_string in self.dataT:
            actual = isUnique(true_string)
            self.assertTrue(actual)

        # false checks
        print("Running false string checks")
        for false_string in self.dataF:
            actual = isUnique(false_string)
            self.assertFalse(actual)

if(__name__ == '__main__'):
    unittest.main()
