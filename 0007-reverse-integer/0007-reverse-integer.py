class Solution:
    def reverse(self, x: int) -> int:
        max_int = pow(2, 31)-1
        min_int = pow(-2, 31)
        if x == 0: return 0
        res = ""
        while x != 0:
            if x < 0:
                res += '-'
                x *= -1
            digit = x % 10
            res += str(digit)
            x = x // 10

        return int(res) if min_int<int(res)<max_int else 0
        