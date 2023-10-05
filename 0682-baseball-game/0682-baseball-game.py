class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                if len(stack) > 1:
                    num1, num2 = stack[-1], stack[-2]
                    stack.append(num1 + num2)
            elif op == "C":
                if stack: stack.pop()
            elif op == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(op))
        return sum(stack)
        