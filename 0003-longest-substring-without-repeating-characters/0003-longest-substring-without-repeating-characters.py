class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp = set()
        l, res = 0, 0

        for r, c in enumerate(s):
            while c in tmp:
                tmp.remove(s[l])
                l += 1
            tmp.add(c)
            res = max(res, len(tmp))
        return res
        
