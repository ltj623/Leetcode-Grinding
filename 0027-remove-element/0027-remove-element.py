class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # while val in nums:
        #     nums.remove(val)

        k = 0

        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k