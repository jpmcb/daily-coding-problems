# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional chars
# And you are given the "true" length of the string

import unittest

def make_url(in_string, true_length):
    string = list(in_string)
    rel_index = len(string) - 1

    for i in reversed(range(true_length)):
        if string[i] == ' ':
            string[rel_index] = '0'
            string[rel_index - 1] = '2'
            string[rel_index - 2] = '%'

            rel_index -= 3
        else:
            string[rel_index] = string[i]
            rel_index -= 1
            
    return ''.join(string)

class Test(unittest.TestCase):
    def test_make_url(self):
        string_in = 'Mr John Smith    '
        expected = 'Mr%20John%20Smith'
        result = make_url(string_in, 13)
        self.assertTrue(result == expected)

if(__name__ == '__main__'):
    unittest.main()