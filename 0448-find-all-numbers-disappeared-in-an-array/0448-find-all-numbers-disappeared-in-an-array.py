class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
        
        for i, num in enumerate(nums):
            if num > 0:
                res.append(i + 1)
        return res

        