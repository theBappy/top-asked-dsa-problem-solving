# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxPath = 0

    def solve(self, root, steps, goLeft):
        if not root:
            return
        self.maxPath = max(self.maxPath, steps)
        if goLeft:
            # Continue zigzag by going left
            self.solve(root.left, steps + 1, False)
            # Start new zigzag by going right
            self.solve(root.right, 1, True)
        else:
            # Continue zigzag by going right
            self.solve(root.right, steps + 1, True)
            # Start new zigzag by going left
            self.solve(root.left, 1, False)

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.solve(root, 0, True)  # Start assuming we can go left first
        self.solve(root, 0, False)  # Start assuming we can go right first
        return self.maxPath
