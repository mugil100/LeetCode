# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx={}
        #create hashmap using the inorder traversal
        for val,i in enumerate(inorder):
            idx[i]=val
        
        def build(inL,inR,poL,poR):
            if inL >inR:
                return None
            rootVal = postorder[poR]
            root = TreeNode(rootVal)

            mid = idx[rootVal]
            leftSize = mid - inL

            root.left = build(inL,mid-1,poL,poL+leftSize-1)
            root.right = build(mid+1,inR,poL+leftSize,poR-1)

            return root

        return build(0,len(inorder)-1,0,len(postorder)-1)



        