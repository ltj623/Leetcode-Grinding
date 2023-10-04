class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = [0] * len(nums)

        for num in nums:
            if freq[num]:
                return num
            freq[num] = 1

        