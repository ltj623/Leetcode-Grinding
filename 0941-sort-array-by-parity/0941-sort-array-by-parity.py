class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0

        for r in range(len(nums)):
            if nums[r] % 2 == 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
        return nums
        