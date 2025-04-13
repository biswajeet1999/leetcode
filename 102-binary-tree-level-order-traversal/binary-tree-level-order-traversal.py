# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     if root is None:
    #         return []

    #     res = []
    #     curLevel = []
    #     queue = []

    #     queue.append(root)
    #     queue.append(None)

    #     while len(queue) > 0:
    #         cur = queue.pop(0)

    #         if cur == None:
    #             if len(queue) > 0:
    #                 queue.append(None)
    #             res.append(curLevel)
    #             curLevel = []
    #             continue
    #         curLevel.append(cur.val)
            
    #         if cur.left:
    #             queue.append(cur.left)
    #         if cur.right:
    #             queue.append(cur.right)

    #     return res

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        res = []
        queue = []

        queue.append(root)

        while len(queue) > 0:
            nodesInCurLevel = len(queue)
            curLevel = []

            while nodesInCurLevel > 0:
                cur = queue.pop(0)
                curLevel.append(cur.val)
                nodesInCurLevel -= 1

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(curLevel)
        
        return res