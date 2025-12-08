/**
 * @param {number[]} edges
 * @return {number}
 */
var longestCycle = function (edges) {
    let result = -1
    const dfs = (u, visited, count, inRecursion) => {
        if (u !== -1) {
            visited[u] = true;
            inRecursion[u] = true;
            const v = edges[u];
            if (v !== -1 && !visited[v]) {
                count[v] = count[u] + 1;
                dfs(v, visited, count, inRecursion);
            } else if (v !== -1 && inRecursion[v] === true) {
                result = Math.max(result, count[u] - count[v] + 1);
            }
            inRecursion[u] = false;
        }
    }
    const n = edges.length;
    const visited = new Array(n).fill(false);
    const count = new Array(n).fill(1);
    const inRecursion = new Array(n).fill(false);
    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, visited, count, inRecursion);
        }
    }
    return result
};