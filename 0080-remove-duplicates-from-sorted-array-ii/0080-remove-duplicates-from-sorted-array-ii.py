class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        while r < len(nums):
            count = 1
            # Count how many same numbers with right pointer
            while r + 1 < len(nums) and nums[r] == nums[r+1]:
                r += 1
                count += 1
            # the maximum times for a number is twice, so move the left pointer
            for _ in range(min(2, count)):
                nums[l] = nums[r]
                l += 1
            r += 1
        return l