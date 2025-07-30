'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
'''
# DFS(pre-order traversal)
# fist left-subtree and then left-subtree
# leftIndex = 2*i
# rightIndex = 2*i+1
# Tc = O(n) [n for serializing and n for de-serializing]
class Codec:
    def serialize(self, root):
        res = []
        def dfs(node):
            if not node:
                res.append("n")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
    def deSerialize(self, data):
        vals = data.split(",")
        self.i = 0
        def dfs():
            if vals[self.i] == 'n':
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()