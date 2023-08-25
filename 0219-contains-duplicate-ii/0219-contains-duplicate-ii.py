class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = {}

        for i, num in enumerate(nums):
            if num in h and abs(h[num] - i) <= k: return True
            h[num] = i
        return False
