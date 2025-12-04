# Using DFS
# T.C : O(m* (V+E)), we try DFS m times in each character
# S.C : O(V+E)

from collections import defaultdict


class Solution:
    def DFSFindMinChar(self, adj, curr_ch, visited):
        visited[ord(curr_ch) - ord('a')] = 1  # mark it as visited
        minChar = curr_ch
        for v in adj[curr_ch]:
            if visited[ord(v) - ord('a')] == 0:
                minChar = min(minChar, self.DFSFindMinChar(adj, v, visited))
        return minChar
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
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
            visited = [0] * 26  # for this ch, none is visited as of now
            minChar = self.DFSFindMinChar(adj, ch, visited)
            result.append(minChar)
        return "".join(result)
