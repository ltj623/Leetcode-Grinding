class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""

        for c in path + '/':
            if c == "/":
                if cur == "..":
                    if stack: stack.pop()
                # skip if cur == "" or cur == "." since its meaningless
                elif cur != "" and cur != ".":
                    stack.append(cur)
                # initiate cur
                cur = ""
            else:
                cur += c
        return '/' + '/'.join(stack)
        