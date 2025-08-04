# Lexicographically smallest equivalent string
# Tc = O(N+M) [M is the length of baseStr] O(26) = O(1) 
# Sc = O(1) or O(N) [for adjacency list as the input size] also O(26)=O(1)
from collections import defaultdict

class Solution:
    def dfsFindMinChar(self, adj, curr_ch, visited):
        visited[ord(curr_ch) - ord('a')] = 1  # mark it visited
        minChar = curr_ch
        
        for v in adj[curr_ch]:
            if visited[ord(v) - ord('a')] == 0:
                minChar = min(minChar, self.dfsFindMinChar(adj, v, visited))
        
        return minChar

    def smallestEquivalentString(self, s1, s2, baseStr):
        n = len(s1)
        m = len(baseStr)
        adj = defaultdict(list)
        
        for i in range(n):
            u = s1[i]
            v = s2[i]
            adj[u].append(v)
            adj[v].append(u)
        
        result = []
        for i in range(m):
            ch = baseStr[i]
            visited = [0] * 26
            minChar = self.dfsFindMinChar(adj, ch, visited)
            result.append(minChar)
        
        return ''.join(result)
