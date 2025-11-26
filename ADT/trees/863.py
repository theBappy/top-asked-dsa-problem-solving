class Solution:
    def __init__(self):
        self.parent = {}

    def addParent(self, root):
        if not root:
            return
        if root.left:
            self.parent[root.left] = root
        self.addParent(root.left)
        if root.right:
            self.parent[root.right] = root
        self.addParent(root.right)

    def collectDistanceNodes(self, target, k, result):
        q = deque([target])
        visited = set([target.val])
        while q:
            n = len(q)
            if k == 0:
                break
            for _ in range(n):
                curr = q.popleft()
                if curr.left and curr.left.val not in visited:
                    q.append(curr.left)
                    visited.add(curr.left.val)
                if curr.right and curr.right.val not in visited:
                    q.append(curr.right)
                    visited.add(curr.right.val)
                if curr in self.parent and self.parent[curr].val not in visited:
                    q.append(self.parent[curr])
                    visited.add(self.parent[curr].val)
            k -= 1
        while q:
            temp = q.popleft()
            result.append(temp.val)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        result = []
        self.addParent(root)
        self.collectDistanceNodes(target, k, result)
        return result
