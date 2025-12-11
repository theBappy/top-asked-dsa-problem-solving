/**
 * @param {number[][]} edges
 * @return {number[]}
 */
var findRedundantConnection = function(edges) {
    const n = edges.length;

    // parent and rank arrays
    const parent = new Array(n + 1);
    const rank = new Array(n + 1);

    // initialize DSU
    for (let i = 1; i <= n; i++) {
        parent[i] = i;
        rank[i] = 0;
    }

    // find with path compression
    const find = (x) => {
        if (parent[x] !== x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    };

    // union by rank
    const Union = (x, y) => {
        const px = find(x);
        const py = find(y);

        if (px === py) return false;

        if (rank[px] > rank[py]) {
            parent[py] = px;
        } else if (rank[py] > rank[px]) {
            parent[px] = py;
        } else {
            parent[py] = px;
            rank[px]++;
        }
        return true;
    };

    // process edges
    for (const [u, v] of edges) {
        if (!Union(u, v)) {
            return [u, v]; // Found redundant edge
        }
    }

    return [];
};
