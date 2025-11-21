class Solution:
    def dfs(self, root: Optional[TreeNode], mp: dict, res: List[TreeNode]) -> str:
        if root is None:
            return "Null"
        s = f"{root.val}, {self.dfs(root.left, mp, res)}, {self.dfs(root.right, mp, res)}"
        if mp[s] == 1:
            res.append(root)
        mp[s] += 1
        return s

    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        mp = defaultdict(int)
        res = []
        self.dfs(root, mp, res)
        return res
