class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        res = []
        ans = 0

        if not nums or target not in nums:
            return [-1, -1]

        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                ans = mid
                r = mid - 1
        res.append(ans)

        l, r = ans + 1, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                ans = mid
                l = mid + 1
        res.append(ans)
        return res
        


         

        
