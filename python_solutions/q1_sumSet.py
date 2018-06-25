# John McBride - jpmmcbride@gmail.com
# June 25th 2018

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

import sys

# Target number
k = int(sys.argv[1])

# Create dictonary with numbers from set as keys
numbers = {}
for element in sys.argv[2:]:
    if(int(element) in numbers):
        # Accounts for the same numbers in a set
        numbers[int(element)] = 'mult'
    else:
        # Gray is used so the same number is not used in the solution
        numbers[int(element)] = 'gray'

    # in the same pass, check if we have a solution
    if(k - int(element) in numbers):
        if(numbers[k - int(element)] == 'white' or numbers[k - int(element)] == 'mult'):
            print("Found match: %d + %d = %d" %(int(element), k - int(element), k))
            break
        else:
            print("There is no match for %d" %(int(element)))
    else:
        print("There is no match for %d" %(int(element)))
        
    # Reset the numbers color
    numbers[int(element)] = 'white'