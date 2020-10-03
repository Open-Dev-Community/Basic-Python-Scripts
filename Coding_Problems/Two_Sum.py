class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i in range(len(nums)):
            n = target - nums[i]
            if n in diff:
                return [diff[n], i]
            else:
                diff[nums[i]] = i