
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        curr = root
        while curr is not None:
            if curr.left is None:
                result.append(curr.val)
                curr = curr.right
            else:
                leftChild = curr.left
                while leftChild.right is not None:
                    leftChild = leftChild.right
                leftChild.right = curr
                temp = curr
                curr = curr.left
                temp.left = None
        return result
