
class Solution:
    def inOrder(self, root, s):
        if root is None:
            return
        if root.left is None and root.right is None:
            s.append(str(root.val) + "_")
            return
        self.inOrder(root.left, s)
        self.inOrder(root.right, s)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        s1 = []
        s2 = []
        self.inOrder(root1, s1)
        self.inOrder(root2, s2)
        return "".join(s1) == "".join(s2)
