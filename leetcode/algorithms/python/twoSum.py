# https://leetcode.com/problems/two-sum/ 

"""
-- Method 1 --

Since there must always be a solution,
for (x1, x2, ... xn), target = xa + xb
So, xa = target - xb
"""
def twoSum(nums, target):
    dict = {}
    for i in range(len(nums)):
        if nums[i] in dict:
            return [i, dict[nums[i]]]
        else:
            dict[target - nums[i]] = i

# Returns [0. 1]
print(twoSum([2,7,11,15], 9))

