
# Time: O(V² log V)
# Space: O(V)

import heapq

class Solution:
    def minCostConnectPoints(self, points):
        """
        Prim's Algorithm to find MST cost.
        Graph is implicit (complete graph).
        """

        V = len(points)

        # Min-heap: (weight, node)
        min_heap = [(0, 0)]

        # Track whether node is already in MST
        in_mst = [False] * V

        total_cost = 0
        edges_used = 0

        while edges_used < V:
            wt, node = heapq.heappop(min_heap)

            # If already in MST, skip
            if in_mst[node]:
                continue

            # Include node in MST
            in_mst[node] = True
            total_cost += wt
            edges_used += 1

            # Try to connect this node to all other nodes
            x1, y1 = points[node]
            for nei in range(V):
                if not in_mst[nei]:
                    x2, y2 = points[nei]
                    dist = abs(x1 - x2) + abs(y1 - y2)

                    # Push edge to heap
                    heapq.heappush(min_heap, (dist, nei))

        return total_cost
