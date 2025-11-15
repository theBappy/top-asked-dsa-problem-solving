# reverse in-order traversal(right -> node -> left)
class Solution:
    def solve(self, root, sum_holder):
        if not root:
            return
        self.solve(root.right, sum_holder)
        sum_holder[0] += root.val
        root.val = sum_holder[0]
        self.solve(root.left, sum_holder)

    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sum_holder = [0]
        self.solve(root, sum_holder)
        return root
