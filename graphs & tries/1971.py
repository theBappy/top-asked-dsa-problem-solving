# Microsoft, Amazon, Adobe, Samsun, Morgan Stanley
# Find if path exists
# Approach-1 (DFS)
# Tc = O(N + E) [building the graph and traversal]
# Sc = O(N + E) [adjacency list is proportional to the number vertices and edges]
from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        # Create an adjacency list representation of the graph
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # A set to keep track of visited nodes
        visited = set()

        def dfs(node):
            # Base case: if we have reached the destination, a path exists
            if node == destination:
                return True
            
            # Mark the current node as visited
            visited.add(node)
            
            # Explore neighbors
            for neighbor in adj[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            
            # If no path from this node leads to the destination, return False
            return False

        # Start the DFS from the source node
        return dfs(source)
    
# Approach-2
# BFS
from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        mp = defaultdict(list)
        for edge in edges:
            u, v = edge
            mp[u].append(v)
            mp[v].append(u)
        
        visited = [False] * n
        q = deque([source])
        visited[source] = True
        
        while q:
            node = q.popleft()
            if node == destination:
                return True
            for V in mp[node]:
                if not visited[V]:
                    q.append(V)
                    visited[V] = True
        
        return False