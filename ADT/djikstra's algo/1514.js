var maxProbability = function (n, edges, succProb, start, end) {

    const adj = new Map();
    for (let i = 0; i < n; i++) adj.set(i, []);

    for (let i = 0; i < edges.length; i++) {
        const [u, v] = edges[i];
        const prob = succProb[i];
        adj.get(u).push([v, prob]);
        adj.get(v).push([u, prob]);
    }

    const result = Array(n).fill(0);
    result[start] = 1;

    const heap = new MaxHeap();
    heap.push([1, start]);

    while (!heap.isEmpty()) {
        const [curProb, curNode] = heap.pop();

        // 🔥 IMPORTANT: skip stale state
        if (curProb < result[curNode]) continue;

        if (curNode === end) return curProb;

        for (const [nextNode, edgeProb] of adj.get(curNode)) {
            const newProb = curProb * edgeProb;
            if (newProb > result[nextNode]) {
                result[nextNode] = newProb;
                heap.push([newProb, nextNode]);
            }
        }
    }

    return 0;
};
