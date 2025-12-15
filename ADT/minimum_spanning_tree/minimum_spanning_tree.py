import heapq

class Solution:
    def spanningTree(self, V, adj):
        """
        V   : number of vertices
        adj : adjacency list where adj[u] = [[v, weight], ...]
        """

        # Min-heap storing (edge_weight, node)
        min_heap = [(0, 0)]  # Start from node 0
        in_mst = [False] * V

        mst_sum = 0

        while min_heap:
            wt, node = heapq.heappop(min_heap)

            # If node already included in MST, skip
            if in_mst[node]:
                continue

            # Include node in MST
            in_mst[node] = True
            mst_sum += wt

            # Explore adjacent edges
            for neighbor, neighbor_wt in adj[node]:
                if not in_mst[neighbor]:
                    heapq.heappush(min_heap, (neighbor_wt, neighbor))

        return mst_sum
