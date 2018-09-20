# String rotation

import unittest

def isSubstring(string, sub):
    print(string, sub)
    return string.find(sub) != -1

def rotate(string, rotate):
    if len(string) != len(rotate):
        return False
    else:
        print(string + string)
        return isSubstring(string + string, rotate)

class Test(unittest.TestCase):

    dataT = [
        ['waterbottle', 'erbottlewat'],
        ['racecar', 'carrace']
    ]

    dataF = [
        ['foo', 'bar'],
        ['foo', 'foofoo']
    ]

    def test_rotate(self):
        for case in self.dataT:
            print(case)
            self.assertTrue(rotate(case[0], case[1]))
        for case in self.dataF:
            self.assertFalse(rotate(case[0], case[1]))
        

if __name__ == "__main__":
    unittest.main()