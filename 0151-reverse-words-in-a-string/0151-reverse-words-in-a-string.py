class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        s = s.strip().split(' ')
        for i, word in enumerate(reversed(s)):
            print(i, word)
            if i != len(s) - 1 and word:
                res += word + ' '
            else:
                res += word
        return res