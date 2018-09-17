# One Away
# Given two strings, write a function to check if they are one edit (or zero edits) away

import unittest

def oneAway(x, y):
    print(x, y)

    x_hash = {}
    for char in x:
        x_hash[char] = 0

    for char in x: 
        x_hash[char] += 1

    y_hash = {}
    for char in y:
        y_hash[char] = 0

    for char in y:
        y_hash[char] += 1

    oneAway = True
    longer = x_hash 
    other = y_hash
    if len(x) >= len(y):
        longer = x_hash
        other = y_hash
    else:
        longer = y_hash
        other = x_hash

    for key in longer:
        for i in range(longer[key]):
            print(key)
            if key not in other:
                if oneAway == False:
                    print("Didn't find it in y table")
                    return False
                else:
                    print("making one away false")
                    oneAway = False

            elif other[key] == 0:
                if oneAway == False:
                    print("The other key is 0!!")
                    return False
                else:
                    oneAway = False

            else:
                longer[key] -= 1
                other[key] -= 1

    return True

class Test(unittest.TestCase):
    dataT = [
        ['pale', 'ple'],
        ['pales', 'pale'],
        ['pale', 'bale'],
        ['helloworld', 'hellowowld'],
        ['puppy', 'poppy']
    ]

    dataF = [
        ['pale', 'bake'],
        ['money', 'monday'],
        ['fire', 'fart'],
        ['helloworld', 'howdywood']
    ]

    def test_isOneAway(self):
        # true checks
        for data in self.dataT:
            result = oneAway(data[0], data[1])
            self.assertTrue(result)

        for data in self.dataF:
            result = oneAway(data[0], data[1])
            self.assertFalse(result)

if(__name__ == '__main__'):
    unittest.main()