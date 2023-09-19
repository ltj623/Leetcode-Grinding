class Solution:
    def partitionString(self, s: str) -> int:
        tmp = set()
        res = 0
        for c in s:
            if c in tmp:
                while tmp:
                    tmp.pop()
                res += 1
            tmp.add(c)
        return res+1