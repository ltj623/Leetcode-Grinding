class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt = {}
        for num in nums:
            if num not in cnt:
                cnt[num] =1
            else:
                return True
        return False
