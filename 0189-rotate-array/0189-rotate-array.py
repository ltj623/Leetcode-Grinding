class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def helper(l, r , nums):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1; r -= 1
        
        k = k % len(nums)
        helper(0, len(nums)-1, nums)
        helper(0, k - 1, nums)
        helper(k, len(nums)-1, nums)
    
      