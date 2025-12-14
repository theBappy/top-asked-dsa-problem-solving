# Google

# Using Dijkstra's Algorithm
# T.C : O(E*log(V))
# S.C : O(V + E)


import heapq
from collections import defaultdict
class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start: int,
        end: int
    ) -> float:

        # Adjacency list: node -> [(neighbor, probability)]
        adj = defaultdict(list)

        for i in range(len(edges)):
            u, v = edges[i]
            prob = succProb[i]
            adj[u].append((v, prob))
            adj[v].append((u, prob))

        # result[i] = maximum probability to reach node i
        result = [0.0] * n
        result[start] = 1.0

        # Max heap using negative probability (Python has min heap)
        maxHeap = [(-1.0, start)]

        while maxHeap:
            curProb, curNode = heapq.heappop(maxHeap)
            curProb = -curProb

            # Early exit if we reach end
            if curNode == end:
                return curProb

            for nextNode, edgeProb in adj[curNode]:
                newProb = curProb * edgeProb

                # If we find a better probability path
                if newProb > result[nextNode]:
                    result[nextNode] = newProb
                    heapq.heappush(maxHeap, (-newProb, nextNode))

        return result[end]     
