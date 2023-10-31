class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h: return False
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            mid = l + (r-l)//2
            total = 0
            for pile in piles:
                total += math.ceil(pile/mid)
            if total <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res        