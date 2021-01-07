def twoSum(self, nums: List[int], target: int) -> List[int]:
    dict = {}
    for i in range(len(nums)):
        if nums[i] in dict:
            return [i, dict[nums[i]]]
        else:
            dict[target - nums[i]] = i

