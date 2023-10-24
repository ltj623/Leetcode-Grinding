class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        h = {0:-1}
        curSum = 0

        for i, num in enumerate(nums):
            curSum += num
            if k != 0:
                curSum %= k
            if curSum in h:
                if i - h[curSum] > 1: return True
            else:
                h[curSum] = i
        return False
        