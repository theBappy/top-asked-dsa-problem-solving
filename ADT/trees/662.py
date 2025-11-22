# Amazon, Flipkart, VmWare

# Level Order Traversal(BFS)

from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([(root, 0)])
        max_width = 0
        while q:
            n = len(q)
            f = q[0][1]
            l = q[-1][1]
            max_width = max(max_width, l - f + 1)
            for _ in range(n):
                curr, i = q.popleft()
                if curr.left:
                    q.append((curr.left, 2 * i + 1))
                if curr.right:
                    q.append((curr.right, 2 * i + 2))
        return max_width
