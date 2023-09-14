class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums) + 1):
            if i not in nums:
                return i

        # Brute Force
        # total = sum(nums)
        # res = 0

        # for i in range(len(nums)+1):
        #     res += i
        # return res - total
        

        # Gassion Law
        # total = sum(nums)
        # return (len(nums) * (len(nums)+1) // 2 - total)
    
        