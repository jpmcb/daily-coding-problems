# Given two strings, check to see if they are anagrams. 
# An anagram is when the two strings can be written using the exact same 
# letters (so you can just rearrange the letters to get a different phrase or word).

# For example:

# "public relations" is an anagram of "crap built on lies."

# "clint eastwood" is an anagram of "old west action"

# Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".


# This solution manually checks for spaces as the dictonary is built
# the strings could also be manually have their white space removed as in anagram_sorted
def anagram(x, y):
    dict = {}

    for char in x:
        if char not in dict and char is not ' ':
            dict[char] = 1
        elif char is not ' ':
            dict[char] += 1

    for char in y:
        if char not in dict and char is not ' ':
            return False
        elif char is not ' ':
            dict[char] -= 1

    for key in dict:
        if dict[key] is not 0:
            return False

    return True

# not the optimal solution as timsort is O(n log n)
# However, this is the optimal memory size solution
def anagram_sorted(x, y):
    x = x.replace(' ', '').lower()
    y = y.replace(' ', '').lower()
    return sorted(x) == sorted(y)

print(anagram('clint eastwood', 'old west action'))
print(anagram('clint eastgood', 'old west action'))
print(anagram('   d  o  g   ', '   g   o   d   '))