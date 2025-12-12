# FlipKart, Amazon

import heapq

class Solution:
    def dijkstra(self, V, edges, src):
        """
        Dijkstra's algorithm using adjacency list and min-heap.
        V: number of vertices
        edges: list of [u, v, w]
        src: source node
        """

        # Build adjacency list
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            # adj[v].append((u, w))  # uncomment for an undirected graph

        # Min heap (distance, node)
        pq = []
        heapq.heappush(pq, (0, src))

        # Initialize distance array
        dist = [float('inf')] * V
        dist[src] = 0

        while pq:
            d, node = heapq.heappop(pq)

            # Skip outdated entries
            if d > dist[node]:
                continue

            # Explore neighbors
            for adjNode, wt in adj[node]:
                if d + wt < dist[adjNode]:
                    dist[adjNode] = d + wt
                    heapq.heappush(pq, (dist[adjNode], adjNode))

        return dist


# using set
# for can erase preview entry of set but cannot do in pq

from sortedcontainers import SortedSet

class Solution:
    def dijkstra(self, V, edges, src):
        """
        Dijkstra using a SortedSet (balanced BST).
        """

        # Build adjacency list
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            # adj[v].append((u, w))  # for undirected graph

        # (distance, node)
        st = SortedSet()
        dist = [float("inf")] * V
        dist[src] = 0

        # Insert source node
        st.add((0, src))

        while st:
            # Get smallest element
            d, node = st[0]
            st.discard((d, node))  # remove it

            # Process neighbors
            for adjNode, wt in adj[node]:
                if d + wt < dist[adjNode]:

                    # Remove old entry if exists
                    if dist[adjNode] != float("inf"):
                        st.discard((dist[adjNode], adjNode))

                    # Update distance
                    dist[adjNode] = d + wt
                    st.add((dist[adjNode], adjNode))

        return dist
