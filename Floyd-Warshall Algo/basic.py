# Multi source shorted path algorithm
# Find the shortest distances between every pair of vertices in a give edge-weighted [directed] graph, can be undirected by making it directed by -> <-
# via each vertex
# Tc = O(V^3)
# Sc = O(V^2)
# Can also detect negative cycle
# Negative cycle => whose resultant of edges is negative eg. 4 + (-3) + (-4) = -3
# if grid[i][i](diagonal element of grid becomes less than 0 cycle exists, bkz src to src should always 0)

INF = float('inf')

def floyd_warshall(V, edges):
    # Initialize distance matrix: dist[u][v] = shortest distance from u to v
    dist = [[INF] * V for _ in range(V)]
    
    # Base cases:
    for u in range(V):
        dist[u][u] = 0  # Distance to self is 0
    for u, v, w in edges:
        dist[u][v] = w  # Direct edge weights
    
    # Floyd-Warshall DP:
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Optional: Check for negative cycles (if any diagonal becomes negative)
    for u in range(V):
        if dist[u][u] < 0:
            return None  # Negative cycle detected
    
    return dist
