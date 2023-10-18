class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        h = {}
        res = 0
        for num in nums:
            res += h.get(num,0)
            h[num] = h.get(num,0) + 1
        return res
        