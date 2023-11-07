class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()

        first_res_len = len(s) % k
        res = s[:first_res_len]
        for i in range(first_res_len, len(s), k):
            if res:
                res += '-'
            res += s[i:i+k]
        return res

        # first_group_len = len(s) % k
        # res = s[:first_group_len]
        # for i in range(first_group_len, len(s), k):
        #     if res:
        #         res += '-'
        #     res += s[i:i+k]
        # return res
        