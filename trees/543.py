# Tc = O(n)
# Sc = O(1) + Recursion Stack(max tree depth -> O(n)) => O(n)
class Solution:
    def solve(self, root, result):
        if root is None:
            return 0
        left = self.solve(root.left)
        right = self.solve(root.right)
        result[0] = max(result[0], left + right)
        return max(left, right) + 1
    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0
        result = [float('-inf')]
        self.solve(root, result)
        return result
