# John McBride
# July 1st 2018

# Given an array of integers, find the first 
# missing positive integer in linear time and constant 
# space. In other words, find the lowest positive integer 
# that does not exist in the array. The array can contain 
# duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.


# --- misingPosInt ----
# Description: After sorting, this function finds the first missing int
# Input: List of ints
# Output: Returns the first found missing int

def missingPosInt(arr):
    missing = 0
    found = False
    
    arr.sort()

    i = 1
    while i < len(arr):
        if arr[i] > 0:
            if arr[i - 1] != arr[i] - 1:
                found = True
                missing = arr[i] - 1
                break
        i += 1

    if not found:
        missing = arr[len(arr) - 1] + 1

    return missing


# ---- Driver Code ----
testing = [3, 4, -1, 1]
other = [1, 2, 0]
big = [7, 5, 3, 1, 0, -1, -3, -5, -7]

print(missingPosInt(testing))
print(missingPosInt(other))
print(missingPosInt(big))