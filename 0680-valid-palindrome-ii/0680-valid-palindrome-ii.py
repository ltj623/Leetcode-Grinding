class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                first, second = s[l:r], s[l+1:r+1]
                return True if first == first[::-1] or second == second[::-1] else False
            l += 1; r-= 1
        return True
        