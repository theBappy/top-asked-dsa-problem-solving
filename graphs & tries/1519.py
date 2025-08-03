# DFS
# Tc = O(V+E) = O(n + (n-1)) = O(n)
# Sc = O(N) [adjacency list]
from collections import defaultdict

class Solution:
    def dfs(self, adj, curr, parent, result, labels, count):
        my_label = labels[curr]
        count_before_visiting_curr_children = count[ord(my_label) - ord('a')]
        
        # Now will explore
        count[ord(my_label) - ord('a')] += 1
        
        for v in adj[curr]:
            if v == parent:
                continue
            self.dfs(adj, v, curr, result, labels, count)
        
        # Time to write after variable
        count_after_visiting_curr_children = count[ord(my_label) - ord('a')]
        result[curr] = count_after_visiting_curr_children - count_before_visiting_curr_children

    def countSubTrees(self, n, edges, labels):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        result = [0] * n
        count = [0] * 26
        self.dfs(adj, 0, -1, result, labels, count)
        return result
