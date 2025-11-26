# Amazon, Meta, Amazon
# Tc = O(log(n) * log(n))

class Solution:
    def leftHeight(self, root):
        if not root:
            return 0
        lh = 0
        temp = root
        while temp:
            temp = temp.left
            lh += 1
        return lh

    def rightHeight(self, root):
        if not root:
            return 0
        rh = 0
        temp = root
        while temp:
            temp = temp.right
            rh += 1
        return rh

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lh = self.leftHeight(root)
        rh = self.rightHeight(root)
        if lh == rh:
            return int(pow(2, lh)) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
