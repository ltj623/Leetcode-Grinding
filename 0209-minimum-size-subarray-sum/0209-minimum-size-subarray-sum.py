class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0
        l = 0
        res = len(nums)
        curSum = 0
        for r, num in enumerate(nums):
            curSum += num
            while curSum >= target:
                res = min(res, r - l + 1)
                curSum -= nums[l]
                l += 1
        return res
            