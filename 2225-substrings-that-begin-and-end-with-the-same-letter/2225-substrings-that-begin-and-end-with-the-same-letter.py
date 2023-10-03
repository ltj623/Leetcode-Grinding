class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        h = {}
        res = 0
        for c in s:
            if c in h:
                res += h[c]
                h[c] += 1
            else:
                h[c] = 1
        return res + len(s)

        