class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num):
            num = str(num)[::-1]
            return int(num)
        
        arr = []
        for i in range(len(nums)):
            arr.append(nums[i] - rev(nums[i]))
        
        h = {}
        res = 0
        MOD = 10**9+7
        for n in arr:
            res = (res + h.get(n, 0)) % MOD
            h[n] = h.get(n, 0) + 1
        
        return res
        
                