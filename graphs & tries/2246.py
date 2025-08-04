# Tc = O(n)
# Sc = O(n)
from collections import defaultdict

class Solution:
    def __init__(self):
        self.result = 0

    def dfs(self, adj, curr, parent, s):
        longest = 0
        second_longest = 0
        
        for child in adj[curr]:
            if child == parent:
                continue
            child_longest_length = self.dfs(adj, child, curr, s)
            if s[child] == s[curr]:
                continue
            if child_longest_length > second_longest:
                second_longest = child_longest_length
            if second_longest > longest:
                longest, second_longest = second_longest, longest
        
        largest_child = max(longest, second_longest) + 1
        only_root = 1
        largest_child_bottom = 1 + longest + second_longest
        self.result = max(self.result, largest_child, only_root, largest_child_bottom)
        
        return max(largest_child, only_root)

    def longestPath(self, parent, s):
        n = len(parent)
        adj = defaultdict(list)
        
        for i in range(1, n):
            u = i
            v = parent[i]
            adj[u].append(v)
            adj[v].append(u)
        
        self.dfs(adj, 0, -1, s)
        return self.result
