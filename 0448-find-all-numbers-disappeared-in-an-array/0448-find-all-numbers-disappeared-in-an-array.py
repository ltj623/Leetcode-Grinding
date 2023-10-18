class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        tmp = [0] * len(nums)
        for num in nums:
            index = num - 1
            tmp[index] = num
        
        for i, num in enumerate(tmp):
            if num == 0:
                res.append(i+1)
        return res

        # res = []
        # for num in nums:
        #     index = abs(num) - 1
        #     nums[index] = - abs(nums[index])
        # print(nums)
        
        # for i, num in enumerate(nums):
        #     if num > 0:
        #         res.append(i + 1)
        # return res
        