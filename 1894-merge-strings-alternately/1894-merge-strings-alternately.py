class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = ""
        while i < len(word1) and j < len(word2):
            res += word1[i]
            res += word2[j]
            i += 1; j += 1
        res += word1[i:] if i < len(word1) else word2[j:]
        return res
        # i, j = 0, 0
        # res = ""
        # while i < len(word1) and j < len(word2):
        #     res += word1[i]
        #     res += word2[j]
        #     i += 1; j += 1
        # res += word1[i:] if i < len(word1) else word2[j:]
        # return res

        