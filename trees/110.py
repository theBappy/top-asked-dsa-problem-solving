
# height-balanced = for every single node left and right subtrees of every node differ in height by no more than 1 (-1,0,1)->tree balance factor(BF)
# Tc = O(n)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root: return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]
            