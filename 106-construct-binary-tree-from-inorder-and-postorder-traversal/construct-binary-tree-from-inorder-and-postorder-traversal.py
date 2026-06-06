class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        idx = {}

        for i,val in enumerate(inorder):
            idx[val] = i

        def build(il,ir,pl,pr):
            if il>ir:
                return None
            #compute the root valu and create the root node
            root_val = postorder[pr]
            root = TreeNode(root_val)

            #find the root val in inorder and find the leftsubtree length
            mid = idx[root_val]
            left_size = mid - il

            #split the left and right subtree
            root.left = build(il,   mid-1,  pl, pl+left_size-1)
            root.right = build(mid+1,   ir, pl+left_size,   pr-1)

            return root
        
        return build(0,len(inorder)-1,0,len(postorder)-1)