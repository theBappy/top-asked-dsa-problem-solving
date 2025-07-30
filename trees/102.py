
# level order traversal(BFS)
# queue (push from back and pop from front)
# O(n)
# O(n) [queue could have upto n/2 elements->the biggest level, n/2 can be rounded to O(n)]
from typing import List
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
        

