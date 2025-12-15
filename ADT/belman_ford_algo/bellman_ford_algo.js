// Microsoft, Amazon, Google
// Tc = O(V*E)
// Sc = O(V)

/**
 * Bellman-Ford Algorithm
 * @param {number} V - Number of vertices
 * @param {number[][]} edges - Each edge = [u, v, w]
 * @param {number} src - Source vertex
 * @return {number[]} - Shortest distances or [-1] if negative cycle exists
 */
function bellmanFord(V, edges, src) {
    const INF = 1e8;

    // Step 1: Initialize distance array
    const dist = new Array(V).fill(INF);
    dist[src] = 0;

    // Step 2: Relax all edges V-1 times
    for (let i = 1; i <= V - 1; i++) {
        let updated = false;

        for (const [u, v, w] of edges) {
            // Relax edge only if u is reachable
            if (dist[u] !== INF && dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                updated = true;
            }
        }

        // Optimization: stop early if no update happened
        if (!updated) break;
    }

    // Step 3: Check for negative weight cycle
    for (const [u, v, w] of edges) {
        if (dist[u] !== INF && dist[u] + w < dist[v]) {
            return [-1]; // Negative cycle detected
        }
    }

    return dist;
}
