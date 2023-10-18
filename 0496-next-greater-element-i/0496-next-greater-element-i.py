class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:    
        nextGreatMap = {}
        stack, res = [], []
        
        for num in nums2:
            while stack and stack[-1] < num:
                nextGreatMap[stack.pop()] = num
            stack.append(num)
        
        for num in nums1:
            res.append(nextGreatMap.get(num, -1))
        return res
