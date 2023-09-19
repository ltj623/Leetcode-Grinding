class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        for k, v in cnt.items():
            if v > 1:
                return k
        return 
        