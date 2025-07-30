class Solution:
    def inorder(self, root, sum, targetSum):
        if root is None:
            return False
        sum += root.val
        if root.left is None and root.right is None:
            return sum == targetSum
        leftSide = self.inorder(root.left, sum, targetSum)
        rightSide = self.inorder(root.right, sum, targetSum)
        return leftSide or rightSide

    def hasPathSum(self, root, targetSum):
        sum = 0
        result = self.inorder(root, sum, targetSum)
        return result