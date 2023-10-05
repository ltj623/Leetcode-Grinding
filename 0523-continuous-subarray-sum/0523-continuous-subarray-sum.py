class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        h = {0: -1}
        prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            if k != 0:
                prefix_sum %= k
            if prefix_sum in h:
                if i - h[prefix_sum] > 1:
                    return True
            else:
                h[prefix_sum] = i
        return False

        