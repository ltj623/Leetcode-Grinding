class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt_violation = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if cnt_violation == 1: return False
                cnt_violation += 1
                if i >= 2 and nums[i-2] > nums[i]:
                    nums[i] = nums[i-1]
        return True

        