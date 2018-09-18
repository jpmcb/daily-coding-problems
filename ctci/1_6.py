# String compression

import unittest

def compress(input):
    # build a hash table
    table = {}
    for char in input:
        if char not in table:
            table[char] = 0

    for char in input:
        table[char] += 1

    # Check if we need to 
    returnSame = False
    for key in table:
        if table[key] != 1:
            returnSame = True

    if (returnSame != True): 
        return input

    #rebuild the compressed string
    returnString = ''
    for key in table:
        returnString += str(key)
        returnString += str(table[key])

    return returnString

# Uses a simple string builder list
# - The test for the randomly dispersed letters will not pass
# - related to how the string builder checks the previous char
def compress_noHash(input):
    strBuilder = []
    counter = 0

    for i in range(len(input)):
        if i != 0 and input[i] != input[i-1]:
            strBuilder.append(input[i-1] + str(counter))
            counter = 0
        counter += 1

    strBuilder.append(input[-1] + str(counter))

    returnString = ''.join(strBuilder)
    if(len(returnString) > len(input)):
        return input
    return returnString


# Test case class
class Test(unittest.TestCase):
    data = [
        ['aaabbbccc', 'a3b3c3'],
        ['aaaazbbccc', 'a4z1b2c3'],
        ['abcdef', 'abcdef'],
        ['aabbccddeeffgghhii', 'a2b2c2d2e2f2g2h2i2'],
        ['aAbBcCdDeE', 'aAbBcCdDeE'],
        ['aAbBcCdDeEaAbBcCdDeE', 'a2A2b2B2c2C2d2D2e2E2']
    ]

    def testCompress(self): 
        print("In normal compress")

        for case in self.data:
            returned = compress(case[0])
            print(returned, case[1])
            self.assertTrue(returned == case[1])

    def testNoHash(self):
        print("In no hash compress")
        for case in self.data:
            returned = compress_noHash(case[0])
            print(returned, case[1])
            self.assertTrue(returned == case[1])

if(__name__ == '__main__'):
    unittest.main()