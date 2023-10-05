class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = float('inf')
        k -= 1
        for i in range(len(nums) - k):
            res = min(res, nums[i+k] - nums[i])
        return res
        