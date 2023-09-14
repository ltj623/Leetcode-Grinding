class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s, stack_t = [], []

        for c in s:
            if c == "#":
                if stack_s: 
                    stack_s.pop()
                else:
                    continue
            else:
                stack_s.append(c)
        print(stack_s)
        for c in t:
            if c == "#":
                if stack_t:
                    stack_t.pop()
                else:
                    continue
            else:
                stack_t.append(c)
        print(stack_t)
        return True if stack_s == stack_t else False

        