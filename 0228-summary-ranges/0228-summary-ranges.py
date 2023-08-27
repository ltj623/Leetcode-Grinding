class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        l, r = 0, 0

        while l < len(nums) and r < len(nums):
            if r + 1 < len(nums) and nums[r + 1] == nums[r] + 1:
                r += 1
            else:
                if nums[l] == nums[r]:
                    res.append(str(nums[l]))
                    l += 1; r += 1
                else:
                    res.append(str(nums[l]) + '->' + str(nums[r]))
                    r += 1
                    l = r
        return res


