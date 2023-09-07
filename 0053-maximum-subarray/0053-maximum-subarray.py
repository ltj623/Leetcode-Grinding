class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub

        # for i in range(1, len(nums)):
        #     if nums[i-1] > 0:
        #         nums[i] += nums[i-1]
        # return max(nums)
        