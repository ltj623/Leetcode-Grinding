class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        h = defaultdict(int)
        unpaired, res = 0, 0

        for word in words:
            if word[0] == word[1]:
                if h[word] > 0:
                    unpaired -= 1
                    res += 4
                    h[word] -= 1
                else:
                    unpaired += 1
                    h[word] += 1
            else:
                if h[word[::-1]] > 0:
                    res += 4
                    h[word[::-1]] -= 1
                else:
                    h[word] += 1
        if unpaired > 0: res += 2
        return res



        