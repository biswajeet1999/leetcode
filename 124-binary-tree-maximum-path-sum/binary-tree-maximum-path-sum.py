# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]):
        return self.maxPathSumHelper(root)[0]

    def maxPathSumHelper(self, root):
        if root is None:
            return -float("inf"), -float("inf")

        maxPathSumInLeft, maxLeftPathSum = self.maxPathSumHelper(root.left)
        maxPathSumInRight, maxRightPathSum = self.maxPathSumHelper(root.right)

        maxPathSum = max(
            maxPathSumInLeft, 
            maxPathSumInRight, 
            root.val + max(maxLeftPathSum, maxRightPathSum), 
            root.val + maxLeftPathSum + maxRightPathSum,
            root.val
        )
        return maxPathSum, max(root.val, root.val + max(maxLeftPathSum, maxRightPathSum))
        
        