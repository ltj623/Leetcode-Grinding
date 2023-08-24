class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i,num in enumerate(nums):
            remain = target - num
            if remain in h:
                return [h[remain], i]
            else:
                h[num] = i
                