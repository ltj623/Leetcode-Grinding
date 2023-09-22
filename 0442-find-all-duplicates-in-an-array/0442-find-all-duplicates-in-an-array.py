class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for k, v in Counter(nums).items():
            if v > 1:
                res.append(k)
        return res
        