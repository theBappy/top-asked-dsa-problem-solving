class Solution {
    bellmanFord(V, edges, src) {
        // Initialize distances from src to all other vertices as infinite
        const result = new Array(V).fill(Infinity);
        result[src] = 0;

        // Relax all edges |V| - 1 times
        for (let count = 0; count < V - 1; count++) {
            for (const [u, v, w] of edges) {
                if (result[u] !== Infinity && result[u] + w < result[v]) {
                    result[v] = result[u] + w;
                }
            }
        }

        // Check for negative weight cycles
        for (const [u, v, w] of edges) {
            if (result[u] !== Infinity && result[u] + w < result[v]) {
                return [-1]; // Return -1 if a negative cycle is detected
            }
        }

        return result;
    }
}
