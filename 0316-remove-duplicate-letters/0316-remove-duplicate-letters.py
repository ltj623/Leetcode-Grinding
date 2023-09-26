class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occur = {}
        for i, c in enumerate(s):
            last_occur[c] = i
        
        stack = []
        visited = set()
        for i, c in enumerate(s):
            if c in visited: continue
            while stack and c < stack[-1] and i < last_occur.get(stack[-1], -1):
                visited.remove(stack.pop())
            visited.add(c)
            stack.append(c)
        return ''.join(stack)
        