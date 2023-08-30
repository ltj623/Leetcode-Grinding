# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q = deque()
        q.append((1, root))
        res = 0

        while q:
            depth, node = q.popleft()
            res = max(res, depth)
            if node.left:
                q.append((depth+1, node.left))
            if node.right:
                q.append((depth+1, node.right))
        return res

    
#         if not root:return 0
#         else:
#             return (1 + max(self.maxDepth(root.left), self.maxDepth(root.right)))

        
        