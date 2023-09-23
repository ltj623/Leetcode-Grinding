class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        #1
        # for k, v in Counter(nums).items():
        #     if v > 1:
        #         res.append(k)
        # return res

        for num in nums:
            num = abs(num)
            if nums[num-1] < 0: res.append(num)
            else:
                nums[num-1] = -nums[num-1]
        return res
        