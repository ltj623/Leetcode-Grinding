class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = [[],[]]
        tmp = []
        for num in nums1:
            if num not in nums2 and num not in tmp:
                tmp.append(num)
        res[0] = tmp
        tmp = []
        for num in nums2:
            if num not in nums1 and num not in tmp:
                tmp.append(num)
        res[1] = tmp
        return res
        