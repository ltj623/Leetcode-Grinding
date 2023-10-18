class Solution:
    def partitionString(self, s: str) -> int:
        tmp = set()
        res = 1
        for c in s:
            if c in tmp:
                res += 1
                tmp = set()
            tmp.add(c)
        return res
            
            