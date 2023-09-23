class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            num = abs(num)
            nums[num-1] = -abs(nums[num-1])

        for i, num in enumerate(nums):
            if num > 0:
                res.append(i+1)
        return res    
        