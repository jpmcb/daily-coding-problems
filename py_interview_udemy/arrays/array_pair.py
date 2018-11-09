# Given an integer array, output all the unique pairs that sum up to a specific value k.

# So the input:
# >> pair_sum([1,3,2,2],4)
# would return 2 pairs:
# >> (1,3)
# >> (2,2)

def pair_sum(x, target):
    # build a table
    dict = {}
    result = []

    for num in x:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1

    for key in dict:
        if dict[key] > 0:
            complement = target - key
            if complement < target:
                if complement in dict and dict[complement] > 0:
                    result.append([key, complement])
                    dict[key] -= 1
                    dict[complement] -= 1

    return result


'''
This is a very interesting approach as it enables us to 
'''

def pair_sum_set(arr ,k):
    if len(arr) < 2:
        return

    # sets for tracking
    seen = set()
    output = set()

    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add( ((min(num, target)), max(num, target)) )

    return output

print(pair_sum([1,2,2,3], 4))
print(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))
print(pair_sum([1,2,3,1],3))

print(pair_sum_set([1,2,2,3], 4))
print(pair_sum_set([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))
print(pair_sum_set([1,2,3,1],3))
print(pair_sum_set([2,3], 4))