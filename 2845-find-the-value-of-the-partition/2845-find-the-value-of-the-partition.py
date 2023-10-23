class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        res = max(nums)
        for i in range(1, len(nums)):
            res = min(res, abs(nums[i] - nums[i-1]))
        return res

        