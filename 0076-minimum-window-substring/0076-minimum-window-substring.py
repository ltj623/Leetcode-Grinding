class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case
        if t == "": return ""

        cnt_t = Counter(t)
        # hashmap we use to track if it equals to the cnt_t
        window = {}
        # if have == need then we know its a substring
        have, need = 0, len(cnt_t)
        res, resLen = [-1, -1], float('infinity')
        l = 0

        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1

            if c in cnt_t and window[c] == cnt_t[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in cnt_t and window[s[l]] < cnt_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res

        return s[l:r+1] if resLen != float('infinity') else ""
            




