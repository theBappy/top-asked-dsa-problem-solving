# Amazon
# Tc = O(n)
# BFS(level order traversal)

from collections import deque
import math
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -math.inf
        result_level = 0
        q = deque([root])
        curr_level = 1
        while q:
            n = len(q)
            level_sum = 0
            for _ in range(n):
                temp = q.popleft()
                level_sum += temp.val
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            if level_sum > max_sum:
                max_sum = level_sum
                result_level = curr_level
            curr_level += 1
        return result_level

# DFS
class Solution:
    def __init__(self):
        self.mp = defaultdict(int)

    def DFS(self, root, level):
        if root is None:
            return
        self.mp[level] += root.val
        self.DFS(root.left, level + 1)
        self.DFS(root.right, level + 1)

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.mp.clear()
        self.DFS(root, 1)
        maxSum = -sys.maxsize
        resul_level = 0
        for level, sum_val in self.mp.items():
            if sum_val > maxSum:
                maxSum = sum_val
                result_level = level
        return result_level
