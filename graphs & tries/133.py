# Google, Amazon, Microsoft
# Deep Copy(cloned)
# DFS/BFS Traversal with Map(adjacency list)
# Tc = O(V+E)
# Sc = O(V) [map will entries one for each node]

# DFS
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def __init__(self):
        self.mp = {}  # Dictionary to map original nodes to their clones

    def dfs(self, node):
        if node in self.mp:
            return self.mp[node]  # Return the clone if it already exists

        # Clone the node
        clone_node = Node(node.val)
        self.mp[node] = clone_node  # Map the original node to the clone

        # Recursively clone the neighbors
        for neighbor in node.neighbors:
            clone_node.neighbors.append(self.dfs(neighbor))

        return clone_node

    def cloneGraph(self, node):
        if not node:
            return None
        return self.dfs(node)
    
# BFS
from collections import deque

class Solution:
    def __init__(self):
        self.mp = {}

    def bfs(self, q):
        while q:
            node = q.popleft()
            clone_node = self.mp[node]  # Get the clone of the current node
            
            for n in node.neighbors:
                if n not in self.mp:
                    clone = Node(n.val)
                    self.mp[n] = clone  # Map the original node to the clone
                    clone_node.neighbors.append(clone)  # Add the clone to the neighbors
                    q.append(n)  # Push the original neighbor to the queue for processing
                else:
                    clone_node.neighbors.append(self.mp[n])  # Add the existing clone to the neighbors

    def cloneGraph(self, node):
        if not node:
            return None

        # Clone the given node 
        clone_node = Node(node.val)

        # Store the mapping of the original node to the cloned node
        self.mp[node] = clone_node

        # BFS approach
        q = deque()
        q.append(node)
        self.bfs(q)
        
        # Return the cloned graph's root node
        return clone_node