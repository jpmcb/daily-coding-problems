# John Mcbride - jpmmcbride@gmail.com
# June 25th 2018

# Question 2 - Product of array (exlude current element)

# Given an array of integers, return a new array such that each element 
# at index i of the new array is the product of all the numbers 
# in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], 
# the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

import sys

master_prod = 1

# Create the master product
for element in sys.argv[1:]:
    master_prod *= int(element)

result = []

# Regenerate list with product of elements (except for current element)
i = 0
for element in sys.argv[1:]:
    result.append(master_prod / int(element))
    i += 1

print(result)
