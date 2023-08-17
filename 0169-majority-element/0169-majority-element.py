class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        for k, v in cnt.items():
            if v > len(nums) / 2:
                return k
        # count = 0
        # candidate = None

        # for num in nums:
        #     if count == 0:
        #         candidate = num
        #     count += 1 if candidate == num else -1
        # return candidate