# Recursion leap of faith

class Solution(object):
    def check(self, head, root):
        if head is None:
            return True
        if root is None:
            return False
        if head.val != root.val:
            return False
        return self.check(head.next, root.left) or self.check(head.next, root.right)
    def isSubPath(self, head, root):
        if root is None:
            return False
        return self.check(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
        