
# BFS (level by level traversal)
from collections import deque
class Solution:
    def isCompleteTree(self, root):
        q = deque([root])
        past = False
        while q:
            node = q.popleft()
            if node is None:
                past = True
            else:
                if past:
                    return False
                q.append(node.left)
                q.append(node.right)
        return True
    
# DFS (first left-subtree then right-subtree traversal)
# root = i
# left-subtree = 2*i
# right-subtree = 2*i+1
###
# index > node.count (not complete binary tree)
# index = node.count (complete binary tree)
###
class Solution:
    def countNodes(self, root):
        if root is None: 
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    def dfs(self, root, i, totalNodes):
        if root is None:
            return True
        if i > totalNodes:
            return False
        return self.dfs(root.left, 2*i, totalNodes) and self.dfs(root.right, 2*i +1, totalNodes)
    def isCompleteTree(self, root):
        totalNodes = self.countNodes(root)
        i = 1
        return self.dfs(root, i, totalNodes)