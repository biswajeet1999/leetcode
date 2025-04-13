# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     return self.diameterOfBinaryTreeUtil(root)[0] - 1

    # def diameterOfBinaryTreeUtil(self, root):
    #     if root is None:
    #         return (0, 0)
        
    #     leftDiameter, leftMaxPath = self.diameterOfBinaryTreeUtil(root.left)
    #     rightDiameter, rightMaxPath = self.diameterOfBinaryTreeUtil(root.right)

    #     maxPath = max(leftMaxPath, rightMaxPath) + 1
    #     curDiameter = 1 + leftMaxPath + rightMaxPath

    #     return (max(curDiameter, leftDiameter, rightDiameter), maxPath)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.diameterOfBinaryTreeUtil(root)[0] - 1

    def diameterOfBinaryTreeUtil(self, root):
        if root is None:
            return (0, 0)
        
        leftDiameter, leftPath = self.diameterOfBinaryTreeUtil(root.left)
        rightDiameter, rightPath = self.diameterOfBinaryTreeUtil(root.right)

        return (
            max(leftDiameter, rightDiameter, leftPath + rightPath + 1),
            1 + max(leftPath, rightPath)
        )


        
