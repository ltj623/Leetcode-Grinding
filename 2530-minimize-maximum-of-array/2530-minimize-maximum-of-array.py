class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = nums[0]
        curSum = nums[0]
        for i in range(1, len(nums)):
            curSum += nums[i]
            res = max(res, math.ceil(curSum / (i+1)))
        return res



        