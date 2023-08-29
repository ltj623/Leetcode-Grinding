class Solution:
    def calculate(self, s: str) -> int:
        num, res = 0, 0
        sign, stack = 1, []

        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c in '+-':
                res += num * sign
                sign = 1 if c == '+' else -1
                num = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif c == ')':
                res += num * sign
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num * sign


        