# Consider an array of non-negative integers. 
# A second array is formed by shuffling the elements 
# of the first array and deleting a random element. 
# Given these two arrays, find which element is missing in the second array.

# Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

# Input:

# finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

# Output:

# 5 is the missing number

# This method won't handle special cases where there are multiple numbers in the array
def finder(x, y):
    if len(x) - 1 != len(y):
        return
    
    seen = set()

    for num in y:
        seen.add(num)

    for num in x:
        if num not in seen:
            return num

    return

# This solution, using the dictonary from collections is a better, more secure approach
import collections
def find_deeper(x, y):
    d = collections.defaultdict(int)

    for num in y: 
        d[num] += 1

    for num in x:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

# This is a very clever XOR solution
def bit_finder(x, y):
    result = 0

    for num in x + y:
        result ^= num

    return result

# print(finder([1, 2, 3, 4, 5], [1, 2, 3, 4]))
# print(finder([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 6, 7, 8, 9]))

# print(find_deeper([1, 2, 3, 4, 5], [1, 2, 3, 4]))
# print(find_deeper([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 6, 7, 8, 9]))

print(bit_finder([1, 2, 3, 4, 5], [1, 2, 3, 4]))
print(bit_finder([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 6, 7, 8, 9]))