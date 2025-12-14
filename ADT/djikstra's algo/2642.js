/**
 * @param {number} n
 * @param {number[][]} edges
 */
var Graph = function (n, edges) {
    this.n = n;
    this.adj = new Map();

    // initialize adjacency list
    for (let i = 0; i < n; i++) {
        this.adj.set(i, []);
    }

    // add initial edges
    for (const [u, v, w] of edges) {
        this.adj.get(u).push([v, w]);
    }
};

/** 
 * @param {number[]} edge
 * @return {void}
 */
Graph.prototype.addEdge = function (edge) {
    const [u, v, w] = edge;
    this.adj.get(u).push([v, w]);
};

/** 
 * @param {number} node1 
 * @param {number} node2
 * @return {number}
 */
Graph.prototype.shortestPath = function (node1, node2) {
    const dist = Array(this.n).fill(Infinity);
    dist[node1] = 0;

    // Min-heap: [distance, node]
    const pq = [[0, node1]];

    while (pq.length > 0) {
        // extract min
        pq.sort((a, b) => a[0] - b[0]);
        const [d, u] = pq.shift();

        if (u === node2) return d;
        if (d > dist[u]) continue;

        for (const [v, w] of this.adj.get(u)) {
            if (dist[v] > d + w) {
                dist[v] = d + w;
                pq.push([dist[v], v]);
            }
        }
    }

    return dist[node2] === Infinity ? -1 : dist[node2];
};
