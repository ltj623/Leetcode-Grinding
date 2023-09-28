class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1
        while l < r:
            if nums[l] % 2 != 0:
                nums.append(nums[l])
                r -= 1
                del(nums[l])
            else:
                l += 1
        return nums

        