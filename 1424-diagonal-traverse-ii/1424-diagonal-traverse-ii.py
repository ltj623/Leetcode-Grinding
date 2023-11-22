class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        rows = len(nums)
        res = []
        h = defaultdict(list)
        for r in range(rows):
            for c in range(len(nums[r])):
                h[r+c].append(nums[r][c])
        
        print(h)
        for key, vals in h.items():
            for val in reversed(vals):
                res.append(val)
        return res
        
        