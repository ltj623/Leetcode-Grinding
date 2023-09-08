# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        q = deque()
        q.append((root, targetSum))

        while q:
            node, curSum = q.popleft()
            # if not node: continue
            if not node.left and not node.right and curSum == node.val:
                return True
            if node.left:
                q.append((node.left, curSum - node.val))
            if node.right:
                q.append((node.right, curSum - node.val))
        return False


        