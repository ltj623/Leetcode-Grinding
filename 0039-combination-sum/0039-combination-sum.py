class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(candidates, [], target, res)
        # self.dfs(candidates, 0, [], target, res)
        return res

    # without index
    def dfs(self, nums, path, target, res):
        if target < 0: return
        if target == 0: res.append(path)

        for i in range(len(nums)):
            self.dfs(nums[i:], path + [nums[i]], target - nums[i], res)
    
    # with index
    # def dfs(self, nums, index, path, target, res):
    #     if target < 0: return
    #     if target == 0: res.append(path)

    #     for i in range(index, len(nums)):
    #         self.dfs(nums, i, path + [nums[i]], target - nums[i], res)