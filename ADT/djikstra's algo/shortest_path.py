#  Shortest Path in Weighted undirected graph(GFG)

import heapq

def shortestPath(n, m, edges):
    """
    Computes the shortest path from node 1 to node n using Dijkstra's algorithm.
    Returns the actual path (list of nodes) or [-1] if no path exists.
    """

    # ---- Build adjacency list ----
    adj = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    # ---- Dijkstra algo ----
    dist = [float('inf')] * (n + 1)
    parent = list(range(n + 1))
    pq = []  # (distance, node)

    dist[1] = 0
    heapq.heappush(pq, (0, 1))

    # ---- Dijkstra's Algorithm ----
    while pq:
        d, node = heapq.heappop(pq)

        # Skip stale entries
        if d != dist[node]:
            continue

        for adjNode, weight in adj[node]:
            if d + weight < dist[adjNode]:
                dist[adjNode] = d + weight
                parent[adjNode] = node
                heapq.heappush(pq, (dist[adjNode], adjNode))

    # ---- No path to n ----
    if dist[n] == float('inf'):
        return [-1]

    # ---- Reconstruct the path ----
    path = []
    curr = n
    while parent[curr] != curr:
        path.append(curr)
        curr = parent[curr]
    path.append(1)
    path.reverse()

    return path
