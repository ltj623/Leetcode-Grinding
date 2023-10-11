class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(candidates, [], target, res)
        return res

    def dfs(self, nums, path, target, res):
        if target < 0: return
        if target == 0: res.append(path)

        for i in range(len(nums)):
            self.dfs(nums[i:], path + [nums[i]], target - nums[i], res)