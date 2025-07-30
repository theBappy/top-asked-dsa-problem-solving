# Tc = O(n) [need to visit every node in the symmetry]
# Sc = O(h) [max depth of recursion stack, in the case of balanced binary tree the height will be O(log.n)]

class Solution:
    def check(self, l, r):
        if not l and not r:
            return True
        if not l or not r:
            return False
        if l.val == r.val and l.left == r.right and l.right == r.left:
            return True
        return False
    def isSymmetric(self,root):
        if not root:
            return True
        return self.check(root.left, root.right)