class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeTwoSortedArrarys(a, b, res):
            i, j, k = 0, 0, 0
            while i < len(a) and j < len(b):
                if a[i] < b[j]:
                    res[k] = a[i]
                    i += 1
                else:
                    res[k] = b[j]
                    j += 1
                k += 1
            res[k:] = a[i:] if i < len(a) else b[j:]

        
        def mergeSort(nums):
            # base case -> Divide to there's only one number
            if len(nums) == 1: return

            mid = len(nums) // 2
            L = nums[:mid]
            R = nums[mid:]

            # Recursive divide
            mergeSort(L)
            mergeSort(R)

            mergeTwoSortedArrarys(L, R, nums)
        
        mergeSort(nums)
        return nums





        