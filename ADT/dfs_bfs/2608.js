/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var findShortestCycle = function (n, edges) {
    const graph = Array.from({ length: n }, () => []);

    // Build the undirected graph
    for (const e of edges) {
        const [u, v] = e;
        graph[u].push(v);
        graph[v].push(u);
    }

    let result = Number.MAX_SAFE_INTEGER;

    // BFS from each node
    for (let start = 0; start < n; start++) {
        const dist = Array(n).fill(-1);
        const parent = Array(n).fill(-1);
        const q = [];

        dist[start] = 0;
        q.push(start);

        while (q.length > 0) {
            const u = q.shift();

            for (const v of graph[u]) {
                if (dist[v] === -1) {
                    dist[v] = dist[u] + 1;
                    parent[v] = u;
                    q.push(v);
                } else if (parent[u] !== v) {
                    // Found a cycle
                    result = Math.min(result, dist[u] + dist[v] + 1);
                }
            }
        }
    }

    return result === Number.MAX_SAFE_INTEGER ? -1 : result;
};