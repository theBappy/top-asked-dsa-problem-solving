class Solution {
    dijkstra(V, edges, src) {
        // Creating an adjacency list
        const adj = Array.from({ length: V }, () => []);
        for (const edge of edges) {
            const [u, v, weight] = edge;
            adj[u].push([v, weight]);
            adj[v].push([u, weight]);
        }
        const pq = [];
        const result = Array(V).fill(Infinity);
        result[src] = 0;
        pq.push([0, src]);
        while (pq.length > 0) {
            const [d, node] = pq.shift();
            if (d > result[node]) {
                continue;
            }
            for (const [adjNode, wt] of adj[node]) {
                if (d + wt < result[adjNode]) {
                    result[adjNode] = d + wt;
                    pq.push([result[adjNode], adjNode]);
                    pq.sort((a, b) => a[0] - b[0]); // Maintaining the priority queue
                }
            }
        }
        return result;
    }
}