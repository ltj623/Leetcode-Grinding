class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        # edge case, important, will cause out of index
        if not s: return True
        for i, c in enumerate(t):
            if c == s[l]:
                l += 1
            if l == len(s): return True
        return False
