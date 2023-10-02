class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True

        increase = 0
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                if increase == -1: return False
                increase = 1
            elif nums[i-1] > nums[i]:
                if increase == 1: return False
                increase = -1
        return True

            
        # if sorted(nums) == nums or sorted(nums, reverse=True) == nums:
        #     return True
        # return False

        