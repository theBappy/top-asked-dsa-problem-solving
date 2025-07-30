# leftN = p
# rightN = q
# then this leftN, rightN containing root is lowest common ancestor

# Else leftN = p
# right = null
# or rightN = q
# left = Null
# not null is LCA

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root == p or root == q:
            return root
        leftN = self.lowestCommonAncestor(root.left, p, q)
        rightN = self.lowestCommonAncestor(root.right, p, q)
        if leftN is not None and rightN is not None:
            return root
        if leftN is not None:
            return leftN
        return rightN
        