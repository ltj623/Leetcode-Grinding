class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        tmp = set()
        if len(s) % 2 == 0:
            for c in s:
                if c not in tmp:
                    tmp.add(c)
                else:
                    tmp.remove(c)
            return True if not tmp else False
        else:
            for c in s:
                if c not in tmp:
                    tmp.add(c)
                else:
                    tmp.remove(c)
            return True if len(tmp) == 1 else False
        

        