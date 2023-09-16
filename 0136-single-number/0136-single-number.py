class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for k, v in Counter(nums).items():
            if v == 1:
                return k
        
        # tmp = set()
        # for num in nums:
        #     if num in tmp:
        #         tmp.remove(num)
        #     else:
        #         tmp.add(num)
        # return tmp.pop()

        