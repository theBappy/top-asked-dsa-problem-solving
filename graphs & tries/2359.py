# Find closest node two given two nodes
# Tc = O(2n) [double call dfs or bfs] overall => O(n)
# DFS approach
class Solution:
    def dfs(self, edges, node, dist, visited):
        visited[node] = True
        v = edges[node]
        if v != -1 and not visited[v]:
            visited[v] = True
            dist[v] = 1 + dist[node]
            self.dfs(edges, v, dist, visited)
    def closestMeetingNode(self, edges, node1, node2):
        n = len(edges)

        dist1 = [float('inf')] * n
        dist2 = [float('inf')] * n

        visited1 = [False] * n
        visited2 = [False] * n

        dist1[node1] = 0
        dist2[node2] = 0

        self.dfs(edges, node1, dist1, visited1)
        self.dfs(edges, node2, dist2, visited2)

        minDistanceNode = -1
        minDistanceNodeTillNow = float('inf')

        for i in range(n):
            maxD = max(dist1[i], dist2[i])
            if minDistanceNodeTillNow > maxD:
                minDistanceNodeTillNow = maxD
                minDistanceNode = i

        return minDistanceNode
    
# BFS 
from collections import deque
class Solution:
    def bfs(self, edges, node, dist):
        n = len(edges)
        q = deque([node])
        dist[node] = 0
        visited = [False] * n
        visited[node] = True
        while q:
            u = q.popleft()
            v = edges[u]
            if v != -1 and not visited[v]:
                visited[v] = True
                dist[v] = 1 + dist[u]
                q.append(v)
    def closestMeetingNode(self, edges, node1, node2):
        n = len(edges)
        dist1 = [float('inf')] * n
        dist2 = [float('inf')] * n
        # Use BFS to calculate distances
        self.bfs(edges, node1, dist1)
        self.bfs(edges, node2, dist2)
        minDistanceNode = -1
        minDistanceNodeTillNow = float('inf')
        for i in range(n):
            maxD = max(dist1[i], dist2[i])
            if minDistanceNodeTillNow > maxD:
                minDistanceNodeTillNow = maxD
                minDistanceNode = i
        return minDistanceNode


