class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)

        for i, c in enumerate(shortest):
            for s in strs:
                if s[i] != c:
                    return shortest[:i]
        return shortest
        