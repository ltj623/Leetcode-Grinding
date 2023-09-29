class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a = []
        a = set(nums1) - set(nums2)
        b = []
        b = set(nums2) - set(nums1)
        res = []
        res.append(a)
        res.append(b)
        return res
        # res = [[],[]]
        # tmp = []
        # for num in nums1:
        #     if num not in nums2 and num not in tmp:
        #         tmp.append(num)
        # res[0] = tmp
        # tmp = []
        # for num in nums2:
        #     if num not in nums1 and num not in tmp:
        #         tmp.append(num)
        # res[1] = tmp
        # return res
        