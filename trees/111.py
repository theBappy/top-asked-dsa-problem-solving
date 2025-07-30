# minimum depth = number of nodes along the shortest path from the root node down to the nearest leaf node


# BFS = level order traversal(when see any nearest leaf node, meaning any left or right node that has no child, immediately return it as the result when traversing level by level)
from collections import deque
class Solution:
    def minDepth(self, root):
        if root is None:
            return 0
        q = deque([root])
        depth = 1
        while q:
            n = len(q)
            for _ in range(n):
                temp = q.popleft()
                if temp.left is None and temp.right is None:
                    return depth
                if temp.left is not None:
                    q.append(temp.left)
                if temp.right is not None:
                    q.append(temp.right)
            depth += 1
        return -1


# DFS = recursive data structure(first left subtree, then right subtree)
# 1 + min(left, right)
class Solution:
    def minDepth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        l = self.minDepth(root.left) if root.left is not None else float('inf')
        r = self.minDepth(root.right) if root.right is not None else float('int')
        return 1 + min(l, r)
