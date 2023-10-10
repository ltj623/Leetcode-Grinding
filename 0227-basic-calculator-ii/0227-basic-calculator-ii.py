class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur = 0
        sign = '+'

        for c in s + '+':
            if c == " ": continue
            elif c.isdigit():
                cur = cur * 10 + int(c)
            else:
                if sign == '-':
                    stack.append(-cur)
                elif sign == '+':
                    stack.append(cur)
                elif sign == '*':
                    stack.append(stack.pop() * cur)
                elif sign == '/':
                    stack.append(int(stack.pop() / cur))
                cur = 0
                sign = c
        return sum(stack)
