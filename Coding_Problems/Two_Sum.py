class Solution:
    def twoSum(self, nums, target):
        diff = {}
        for i in range(len(nums)):
            n = target - nums[i]
            if n in diff:
                return [diff[n], i]
            else:
                diff[nums[i]] = i