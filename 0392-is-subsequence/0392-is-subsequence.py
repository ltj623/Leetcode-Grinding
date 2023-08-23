class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        if not s: return True
        for i, c in enumerate(t):
            if c == s[l]:
                l += 1
            if l == len(s): return True
        return False
        # l = 0
        # if not s: return True

        # for r in range(len(t)):
        #     if s[l] == t[r]:
        #         l += 1
        #     if l == len(s): return True
        # return False