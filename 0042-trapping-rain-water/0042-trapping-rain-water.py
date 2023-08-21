class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3: return 0
        l, r = 0, len(height)-1
        maxL, maxR = height[l], height[r]
        res = 0

        while l < r:
            maxL, maxR = max(maxL, height[l]), max(maxR, height[r])
            if maxL < maxR:
                res += maxL - height[l]
                l += 1
            else:
                res += maxR - height[r]
                r -= 1
        return res