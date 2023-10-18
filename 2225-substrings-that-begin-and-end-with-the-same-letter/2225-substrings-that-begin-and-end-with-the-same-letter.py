class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        h = {}
        res = 0
        for c in s:
            h[c] = h.get(c,0) + 1
            res += h[c]
        return res
        