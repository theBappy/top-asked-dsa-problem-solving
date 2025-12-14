const { PriorityQueue } = require('@datastructures-js/priority-queue');

/**
 * @param {number[][]} times
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var networkDelayTime = function (times, n, k) {
    // Adjacency list
    const adj = new Map();
    for (const [u, v, w] of times) {
        if (!adj.has(u)) adj.set(u, []);
        adj.get(u).push([v, w]);
    }

    // Distance array
    const dist = Array(n + 1).fill(Infinity);
    dist[k] = 0;

    // Min Priority Queue (compare by distance)
    const pq = new PriorityQueue((a, b) => a[0] - b[0]);
    pq.enqueue([0, k]); // [distance, node]

    // Dijkstra
    while (!pq.isEmpty()) {
        const [currDist, node] = pq.dequeue();

        if (currDist > dist[node]) continue;

        for (const [next, weight] of (adj.get(node) || [])) {
            const newDist = currDist + weight;
            if (newDist < dist[next]) {
                dist[next] = newDist;
                pq.enqueue([newDist, next]);
            }
        }
    }

    // Result
    let ans = 0;
    for (let i = 1; i <= n; i++) {
        if (dist[i] === Infinity) return -1;
        ans = Math.max(ans, dist[i]);
    }

    return ans;
};
