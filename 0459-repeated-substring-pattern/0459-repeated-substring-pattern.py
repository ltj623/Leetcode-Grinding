class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s_fold = "".join((s[1:], s[:-1]))
        return True if s in s_fold else False
        
        