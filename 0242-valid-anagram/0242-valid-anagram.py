class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return True if Counter(s) == Counter(t) else False
        cnt_s = Counter(s)
        for c in t:
            if c not in cnt_s: return False
            cnt_s[c] -= 1
            if cnt_s[c] == 0: del cnt_s[c]
        return True if not cnt_s else False




        h = {}
        for c in s:
            h[c] = h.get(c,0) + 1
        for c in t:
            if c not in h:
                return False
            else:
                h[c] -= 1
                if h[c] == 0:
                    del h[c]
        return True if not h else False

        