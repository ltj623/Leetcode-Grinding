# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return 0
        q = deque()
        q.append(root)
        res = []

        while q:
            curTotal = 0
            count = len(q)
            for _ in range(len(q)):
                node = q.popleft()
                curTotal += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(curTotal / count)
        return res

        