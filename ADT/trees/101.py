
class Solution:
    def check(self, l, r):
        if l is None and r is None:
            return True
        if l is None or r is None:
            return False
        if l.val == r.val and self.check(l.left, r.right) and self.check(l.right, r.left):
            return True
        return False
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.check(root.left, root.right)