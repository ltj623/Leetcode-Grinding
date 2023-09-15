# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node: Optional[TreeNode], l, r):
            if not node: return True
            if not l<node.val<r: return False

            return check(node.left, l, node.val) and check(node.right, node.val, r)
        return check(root, float('-inf'), float('inf'))