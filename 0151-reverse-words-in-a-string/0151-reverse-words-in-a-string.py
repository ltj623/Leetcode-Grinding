class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        s = s.strip().split(' ')
        for i, c in enumerate(s[::-1]):
            if c == "": continue
            res += c + " "
        
        return res[:-1]