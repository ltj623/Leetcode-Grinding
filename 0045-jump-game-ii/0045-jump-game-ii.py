class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0

        # [2,3,1,1,4]
        # the first will be [2] -> 0 jump
        # then [3, 1] -> l = 0 + 1, r = 0 + 2, 1 jump
        # last [1, 4] -> l = 2 + 1, r = 1 + 3, 2 jump

        # r should less than the last index, cuz if it goes to the last index it will make another jump
        while r < len(nums) - 1:
            farthest = 0
            # the level between l and r pointer, get the maximum
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            # update the l and r pointer
            l = r + 1
            r = farthest
            res += 1
        return res