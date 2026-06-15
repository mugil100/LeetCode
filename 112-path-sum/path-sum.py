# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        summ = 0
        def checkVal(root,summ):
            
            if not root:
                return False
            summ += root.val
            if not root.left and not root.right:
                return summ == targetSum
            return checkVal(root.left, summ) or checkVal(root.right, summ)
            
        return checkVal(root, summ)


            

            
        