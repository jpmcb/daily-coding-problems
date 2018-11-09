# Given an array of integers (positive and negative) find the largest continuous sum.

def sum(arr):
    if len(arr) == 0:
        return None
    
    max_sum = cur_sum = arr[0]

    for num in arr[1:]:
        cur_sum = max(cur_sum + num, num)
        max_sum = max(cur_sum, max_sum)

    return max_sum