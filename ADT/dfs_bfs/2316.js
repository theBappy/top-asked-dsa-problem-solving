/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var countPairs = function(n, edges) {
    const adj = Array.from({ length: n }, () => []);

    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const visited = Array(n).fill(false);

    function dfs(u) {
        visited[u] = true;
        let size = 1;
        for (const v of adj[u]) {
            if (!visited[v]) {
                size += dfs(v);
            }
        }
        return size;
    }

    let remainingNodes = n;
    let result = 0;

    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            const size = dfs(i);
            result += size * (remainingNodes - size);
            remainingNodes -= size;
        }
    }

    return result;
};
