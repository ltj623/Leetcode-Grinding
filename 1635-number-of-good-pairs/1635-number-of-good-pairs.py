class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        h = {}
        res = 0

        for i, num in enumerate(nums):
            if num in h:
                res += h[num]
                h[num] += 1
            else:
                h[num] = 1
        return res