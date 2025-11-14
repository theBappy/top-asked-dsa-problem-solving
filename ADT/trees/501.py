class Solution:
    def __init__(self):
        self.mp = defaultdict(int)

    def dfs(self, root: Optional[TreeNode]):
        if not root:
            return
        self.dfs(root.left)
        self.mp[root.val] += 1
        self.dfs(root.right)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.dfs(root)
        result = []
        maxFreq = 0
        for key, value in self.mp.items():
            if value > maxFreq:
                maxFreq = value
                result = [key]
            elif value == maxFreq:
                result.append(key)
        return result






class Solution:
    def __init__(self):
        self.currNum = 0
        self.currFreq = 0
        self.maxFreq = 0
        self.result = []

    def dfs(self, root: Optional[TreeNode]):
        if not root:
            return
        self.dfs(root.left)
        if root.val == self.currNum:
            self.currFreq += 1
        else:
            self.currNum = root.val
            self.currFreq = 1
        if self.currFreq > self.maxFreq:
            self.result = []
            self.maxFreq = self.currFreq
        if self.currFreq == self.maxFreq:
            self.result.append(root.val)
        self.dfs(root.right)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.dfs(root)
        return self.result
