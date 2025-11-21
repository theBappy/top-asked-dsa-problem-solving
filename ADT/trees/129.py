# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find(self, root, curr):
        if not root:
            return 0
        curr = curr * 10 + root.val
        if root.left is None and root.right is None:
            return curr
        left_sum = self.find(root.left, curr)
        right_sum = self.find(root.right, curr)
        return left_sum + right_sum

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.find(root, 0)
