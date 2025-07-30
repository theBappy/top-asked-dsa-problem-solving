class Solution:
    def deleteHelper(self,root, to_delete_set, result):
        if not root:
            return None
        root.left = self.deleteHelper(root.left, to_delete_set, result)
        root.right = self.deleteHelper(root.right, to_delete_set, result)
        if root.val in to_delete_set:
            if root.left:
                result.append(root.left)
            if root.right:
                result.append(root.right)
            return None
        else:
            return None
    def delNodes(self, root, to_delete):
        result = []
        to_delete_set = set(to_delete)
        root = self.deleteHelper(root,to_delete_set, result)
        if root:
            result.append(root)
        return result