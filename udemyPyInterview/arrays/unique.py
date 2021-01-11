# Given a string, determine if it is compreised of all 
# unique characters. For example, the string 
# 'abcde' has all unique characters and should return True. 
# The string 'aabcde' contains duplicate characters
# and should return false.

import collections

def unique(s):
    if len(s) == 0:
        return None

    d = collections.defaultdict(int)

    for char in s:
        d[char] += 1

    for key in d:
        if d[key] > 1:
            return False

    return True

print(unique('abcdef'))
print(unique('aabcde'))