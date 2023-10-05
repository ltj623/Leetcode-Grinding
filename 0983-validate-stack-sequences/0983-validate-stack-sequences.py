class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        index = 0
        stack = []
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and index < len(popped) and popped[index] == stack[-1]:
                print(stack)
                stack.pop()
                index += 1
        return True if not stack else False