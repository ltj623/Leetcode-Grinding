class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum, rightsum = 0, sum(nums)
        for i, num in enumerate(nums):
            rightsum -= num
            if leftsum == rightsum:
                return i
            leftsum += num
        return -1
        