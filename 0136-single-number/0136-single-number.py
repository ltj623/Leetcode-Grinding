class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tmp = set()
        for num in nums:
            if num in tmp:
                tmp.remove(num)
            else:
                tmp.add(num)
        return tmp.pop()

        