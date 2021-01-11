# Practice 1
# Write a recursive function which takes an 
# integer and computes the cumulative sum of 0 to that integer

def rec_sum(n):
    # base case
    if n == 0:
        return 0

    # recursive case
    else:
        return n + rec_sum(n - 1)

print(rec_sum(4))

# Practice 2
# Given an integer, create a function which returns 
# the sum of all the individual digits in that integer. 
# For example: if n = 4321, return 4+3+2+1

def sum_func(n):
    # base case
    if n < 10:
        return n

    # recursive case
    else:
        return (n % 10) + sum_func(n // 10)

print(sum_func(4321))

# Practice 3
# Create a function called word_split() which takes in a 
# string phrase and a set list_of_words. The function will 
# then determine if it is possible to split the string in 
# a way in which words can be made from the list of words. 
# You can assume the phrase will only contain words found 
# in the dictionary if it is completely splittable.

def word_split(s, arr):
    pass