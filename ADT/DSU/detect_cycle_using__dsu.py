from typing import List

class Solution:
    def __init__(self):
        self.parent = []
        self.rank = []

    def find(self, x: int) -> int:
    	if self.parent[x] == x:
    		return x
    	# path compression by caching
    	self.parent[x] = self.find(self.parent[x])
    	return self.parent[x]
        
    def Union(self, x: int, y: int) -> None:
    	x_parent = self.find(x)
    	y_parent = self.find(y)

    	# union find by rank
    	if self.rank[x_parent] > self.rank[y_parent]:
    		self.parent[y_parent] = x_parent
    	elif self.rank[x_parent] < self.rank[y_parent]:
    		self.parent[x_parent] = y_parent
    	else:
    		self.parent[x_parent] = y_parent
    		self.rank[y_parent] += 1

    # Function to detect cycle using DSU in an undirected graph.
    def detectCycle(self, V: int, adj: List[List[int]]) -> bool:
    	self.parent = list(range(V))
    	self.rank = [0] * V

    	for u in range(V):
    		for v in adj[u]:
    			if u < v:
    				if self.find(u) == self.find(v):
    					return True

    				else:
    					self.Union(u, v)
    	return False
