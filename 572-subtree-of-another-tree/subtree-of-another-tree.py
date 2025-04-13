# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res1 = []
        res2 = []
        self.preOrder(root, res1)
        self.preOrder(subRoot, res2)

        return "".join(res2) in "".join(res1)

    def preOrder(self, root, res):
        if not root:
            res.append("*")
            return
        
        res.append("(" + str(root.val) + ")")
        self.preOrder(root.left, res)
        self.preOrder(root.right, res)
    
            