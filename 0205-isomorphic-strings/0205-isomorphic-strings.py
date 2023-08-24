class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t, t_to_s = {}, {}
        for i, c in enumerate(s):
            if c not in s_to_t and t[i] not in t_to_s:
                s_to_t[c] = t[i]
                t_to_s[t[i]] = c
            elif c in s_to_t and s_to_t[c] == t[i]:
                continue
            else:
                return False
        return True
            


        # m1, m2 = [], []

        # for i in range(len(s)):
        #     m1.append(s.index(s[i]))
        #     m2.append(t.index(t[i]))
        # return m1 == m2