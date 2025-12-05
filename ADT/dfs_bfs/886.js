
//Using BFS
// Tc = O(V+E)
/**
 * @param {number} n
 * @param {number[][]} dislikes
 * @return {boolean}
 */
var possibleBipartition = function (n, dislikes) {
    const adj = new Map()
    const isBipartite = (adj, node, color) => {
        const que = [];
        que.push(node);
        color[node] = 1; // red
        while (que.length > 0) {
            const u = que.shift();
            for (const v of (adj.get(u) || [])) {
                if (color[v] === color[u])
                    return false;
                if (color[v] === -1) {
                    que.push(v);
                    color[v] = 1 - color[u];
                }
            }
        }
        return true;
    }
    for (const vec of dislikes) {
        const u = vec[0]
        const v = vec[1]
        if (!adj.has(u)) adj.set(u, [])
        if (!adj.has(v)) adj.set(v, [])
        adj.get(u).push(v)
        adj.get(v).push(u)
    }
    const color = new Array(n + 1).fill(-1)
    for (let i = 0; i <= n; i++) {
        if (color[i] === -1) {
            if (!isBipartite(adj, i, color)) {
                return false
            }
        }
    }
    return true
};