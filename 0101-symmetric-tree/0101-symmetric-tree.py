# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isS(l, r):
            if not l and not r: return True
            if l and r and l.val == r.val:
                return isS(l.left, r.right) and isS(l.right, r.left)
        if not root: 
            return True
        else:
            return isS(root.left, root.right)
        