class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        a, b = list(a), list(b)
        carry = 0

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            res = str(carry % 2) + res
            carry //= 2
        return res