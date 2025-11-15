# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, root: Optional[TreeNode], vec: List[int]) -> None:
        if not root:
            return
        self.inOrder(root.left, vec)
        vec.append(root.val)
        self.inOrder(root.right, vec)

    def constructBST(self, l: int, r: int, vec: List[int]) -> Optional[TreeNode]:
        if l > r:
            return None
        mid = l + (r - l) // 2
        root = TreeNode(vec[mid])
        root.left = self.constructBST(l, mid - 1, vec)
        root.right = self.constructBST(mid + 1, r, vec)
        return root

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        vec = []
        self.inOrder(root, vec)
        l = 0
        r = len(vec) - 1
        return self.constructBST(l, r, vec)
