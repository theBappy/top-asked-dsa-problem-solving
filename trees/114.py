class Solution:
    def preorder(self, root, result):
        if root is None:
            return
        result.append(root.val)
        self.preorder(root.left, result)
        self.preorder(root.right, result)

    def preorderTraversal(self, root):
        result = []
        self.preorder(root, result)
        return result