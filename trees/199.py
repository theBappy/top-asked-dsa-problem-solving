# Level Order Traversal(BFS)
# Tc = O(n)
# Sc = O(n)
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if root is None:
            return []
        result = []
        que = deque([root])
        while que:
            n = len(que)
            node = None
            for _ in range(n):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            result.append(node.val)
        return result

# Pre Order Traversal(DFS)
# Tree level(eg.3) = output level(eg.3) bkz each level first element will be seen from right side view
class Solution:
    def preOrder(self, root, level, result):
        if root is None:
            return
        if len(result) < level:
            result.append(root.val)
        self.preOrder(root.right, level + 1, result)
        self.preOrder(root.left, level + 1, result)

    def rightSideView(self, root):
        result = []
        self.preOrder(root, 1, result)
        return result

