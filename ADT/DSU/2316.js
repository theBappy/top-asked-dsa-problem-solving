var countPairs = function (n, edges) {
    const parent = new Array(n).fill(0).map((_, i) => i);
    const rank = new Array(n).fill(1);

    const find = (x) => {
        if (parent[x] !== x) parent[x] = find(parent[x]);
        return parent[x];
    };

    const Union = (x, y) => {
        const px = find(x), py = find(y);
        if (px !== py) {
            if (rank[px] > rank[py]) parent[py] = px;
            else if (rank[px] < rank[py]) parent[px] = py;
            else {
                parent[py] = px;
                rank[px]++;
            }
        }
    };

    for (const [u, v] of edges) Union(u, v);

    const mp = new Map();
    for (let i = 0; i < n; i++) {
        const head = find(i);
        mp.set(head, (mp.get(head) || 0) + 1);
    }

    let result = 0n;
    let remaining = BigInt(n);

    for (const size of mp.values()) {
        const sz = BigInt(size);
        result += sz * (remaining - sz);
        remaining -= sz;
    }

    return Number(result); 
};
