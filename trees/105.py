# Tc = O(n)
# Sc = O(n)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        self.preorder_idx = 0

        def solve(start: int, end: int) -> TreeNode:
            if start > end:
                return None
            root_val = preorder[self.preorder_idx]
            self.preorder_idx += 1
            root = TreeNode(root_val)
            root_inorder_idx = inorder_map[root_val]
            root.left = solve(start, root_inorder_idx - 1)
            root.right = solve(root_inorder_idx + 1, end)
            return root
        n = len(preorder)
        return solve(0, n - 1)