class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        tmp = set()
        for c in s:
            if c not in tmp:
                tmp.add(c)
            else:
                tmp.remove(c)
        return len(tmp) <= 1
        

        