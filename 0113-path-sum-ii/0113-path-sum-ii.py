# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        q = deque()
        q.append((root, targetSum, []))
        res = []

        while q:
            node, curSum, path = q.popleft()
            if not node.left and not node.right and curSum == node.val:
                res.append(path + [node.val])
            else:
                if node.left:
                    q.append((node.left, curSum- node.val, path + [node.val]))
                if node.right:
                    q.append((node.right, curSum- node.val, path + [node.val]))
        return res

        