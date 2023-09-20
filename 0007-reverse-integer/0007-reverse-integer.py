class Solution:
    def reverse(self, x: int) -> int:
        max_int = pow(2, 31)-1
        min_int = pow(-2, 31)
        sign = 1
        if x < 0: sign = -1
        res = ""
        for c in str(x)[::-1]:
            if c.isdigit():
                res += c
        return int(res) * sign if min_int<int(res) * sign <max_int else 0
        # max_int = pow(2, 31)-1
        # min_int = pow(-2, 31)
        # if x == 0: return 0
        # res = ""
        # while x != 0:
        #     if x < 0:
        #         res += '-'
        #         x *= -1
        #     digit = x % 10
        #     res += str(digit)
        #     x = x // 10

        # return int(res) if min_int<int(res)<max_int else 0
        