class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] #[num, cur_min]
        cur_min = nums[0]
        for num in nums[1:]:
            while stack and num >= stack[-1][0]:
                stack.pop()
            if stack and num > stack[-1][-1]:
                return True
            cur_min = min(cur_min, num)
            stack.append([num, cur_min])
        return False
            


        