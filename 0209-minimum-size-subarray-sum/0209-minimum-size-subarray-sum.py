class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0
        l, res = 0, len(nums) + 1
        cursum = 0
        for r in range(len(nums)):
            cursum += nums[r]
            while cursum >= target:
                res = min(r-l+1, res)
                cursum -= nums[l]
                l += 1
        return res
