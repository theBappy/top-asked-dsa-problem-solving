class Solution:
    def solve(
        self,
        inorder: List[int],
        postorder: List[int],
        inStart: int,
        inEnd: int,
        postStart: int,
        postEnd: int,
    ) -> Optional[TreeNode]:
        if inStart > inEnd:
            return None
        root = TreeNode(postorder[postEnd])
        i = inStart
        while i <= inEnd:
            if inorder[i] == root.val:
                break
            i += 1
        leftSize = i - inStart
        rightSize = inEnd - i
        root.left = self.solve(
            inorder, postorder, inStart, i - 1, postStart, postStart + leftSize - 1
        )
        root.right = self.solve(
            inorder, postorder, i + 1, inEnd, postEnd - rightSize, postEnd - 1
        )
        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        inStart = 0
        inEnd = n - 1
        postStart = 0
        postEnd = n - 1
        return self.solve(inorder, postorder, inStart, inEnd, postStart, postEnd)
