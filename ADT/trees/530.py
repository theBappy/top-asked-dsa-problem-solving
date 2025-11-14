
class Solution(object):
    def __init__(self):
        self.minDiff = float('inf')
        self.prev = None
    def inOrder(self, root):
        if not root:
            return 
        self.inOrder(root.left)
        if self.prev is not None:
            self.minDiff = min(self.minDiff, root.val - self.prev.val)
        self.prev = root
        self.inOrder(root.right)
    def getMinimumDifference(self, root):
        self.minDiff = float('inf')
        self.prev = None
        self.inOrder(root)
        return self.minDiff
        