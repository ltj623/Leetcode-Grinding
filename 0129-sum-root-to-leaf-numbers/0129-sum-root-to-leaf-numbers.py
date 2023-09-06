# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curNode: Optional[TreeNode], num: int):
            if not curNode.left and not curNode.right:
                self.res += num * 10 + curNode.val
                return
            
            if curNode.left:
                dfs(curNode.left, num * 10 + curNode.val)
            if curNode.right:
                dfs(curNode.right, num * 10 + curNode.val)
        
        dfs(root, 0)
        return self.res
        