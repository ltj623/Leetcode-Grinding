class Solution:
    def longestPalindrome(self, s: str) -> int:
        tmp = set()
        for c in s:
            if c in tmp:
                tmp.remove(c)
            else:
                tmp.add(c)
        if not tmp: 
            return len(s)
        else:
            return len(s) - len(tmp) + 1