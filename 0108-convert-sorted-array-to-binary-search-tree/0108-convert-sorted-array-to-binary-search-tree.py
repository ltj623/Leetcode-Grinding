# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def rec(nums, l, r):
            if l <= r:
                mid = l+(r-l)//2
                node = TreeNode(nums[mid])
                node.left = rec(nums, l, mid-1)
                node.right = rec(nums, mid+1, r)
                return node
        return rec(nums, 0, len(nums)-1)

