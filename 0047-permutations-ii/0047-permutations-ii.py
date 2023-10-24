class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(counter, path):
            if len(path) == len(nums):
                res.append(path)
                return
            for key in counter:
                if counter[key]:
                    counter[key] -= 1
                    dfs(counter, path + [key])
                    counter[key] += 1
        
        dfs(Counter(nums), [])
        return res