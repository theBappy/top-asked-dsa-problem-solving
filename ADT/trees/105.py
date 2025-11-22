class Solution:
    def solve(
        self,
        preorder: List[int],
        inorder: List[int],
        preStart: int,
        preEnd: int,
        inStart: int,
        inEnd: int,
    ) -> Optional[TreeNode]:
        
        if preStart > preEnd or inStart > inEnd:
            return None

        root = TreeNode(preorder[preStart])

        # Find root in inorder
        i = inStart
        while i <= inEnd:
            if inorder[i] == root.val:
                break
            i += 1

        leftSize = i - inStart

        # LEFT SUBTREE
        root.left = self.solve(
            preorder,
            inorder,
            preStart + 1,                 
            preStart + leftSize,
            inStart,
            i - 1
        )

        # RIGHT SUBTREE
        root.right = self.solve(
            preorder,
            inorder,
            preStart + leftSize + 1,      
            preEnd,
            i + 1,
            inEnd
        )

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        return self.solve(preorder, inorder, 0, n - 1, 0, n - 1)
