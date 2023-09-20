class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l, r = 0, 0
        curSum = 0
        target = sum(nums) - x
        max_window = -1

        for r in range(len(nums)):
            curSum += nums[r]

            while l <= r and curSum > target:
                curSum -= nums[l]
                l += 1

            if curSum == target:
                max_window = max(max_window, r - l + 1)
        return -1 if max_window == -1 else len(nums) - max_window



        