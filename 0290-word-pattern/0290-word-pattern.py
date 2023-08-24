class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.strip().split(" ")
        if len(s) != len(pattern): return False
        s_to_p, p_to_s = {}, {}
        for i, c in enumerate(pattern):
            if c not in p_to_s and s[i] not in s_to_p:
                p_to_s[c] = s[i]
                s_to_p[s[i]] = c
            elif c in p_to_s and p_to_s[c] == s[i]:
                continue
            else:
                return False
        return True
                
        # #one hashMap
        # s = s.split(" ")
        # h = {}
        # if len(s) != len(pattern): return False
        # if len(set(s)) != len(set(pattern)): return False
        # for i in range(len(s)):
        #     if s[i] not in h:
        #         h[s[i]] = pattern[i]
        #     elif h[s[i]] != pattern[i]:
        #         return False
        # return True

        # use the same way - 205. Isomorphic Strings