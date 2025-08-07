# Google
# For probability needs to multiply
# In dijkstra we do sum but here just needs to multiply
# In this problem max probability instead minimum distance
# need to use max heap instead min heap
# Tc = O(N+E).logN
# Sc = O(N+E) [adj list and result vector]
import heapq
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start: int, end: int) -> float:
        # Create an adjacency list
        adj = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            prob = succProb[i]
            adj[u].append((v, prob))
            adj[v].append((u, prob))
        
        # Max heap to store probabilities
        max_heap = []
        heapq.heappush(max_heap, (-1.0, start))  # Use negative to simulate max-heap
        result = [0.0] * n
        result[start] = 1.0  # Probability to reach start is 100%
        
        while max_heap:
            currProb, currNode = heapq.heappop(max_heap)
            currProb = -currProb  # Convert back to positive
            
            # If we reach the end node, return the probability
            if currNode == end:
                return currProb
            
            for adjNode, adjProb in adj[currNode]:
                newProb = currProb * adjProb
                if result[adjNode] < newProb:
                    result[adjNode] = newProb
                    heapq.heappush(max_heap, (-newProb, adjNode))  # Push negative for max-heap
        
        return 0.0  # If end is not reachable


