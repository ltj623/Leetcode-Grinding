class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        cur_zero_subarrys = 0

        for num in nums:
            if num == 0:
                cur_zero_subarrys += 1
                res += cur_zero_subarrys
            else:
                cur_zero_subarrys = 0
        return res
        