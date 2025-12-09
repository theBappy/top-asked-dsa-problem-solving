/**
 * @param {string[][]} equations
 * @param {number[]} values
 * @param {string[][]} queries
 * @return {number[]}
 */
var calcEquation = function (equations, values, queries) {
    const dfs = (adj, src, dst, visited, product, ans) => {
        if (visited.has(src)) return
        visited.add(src)
        if (src === dst) {
            ans.value = product
            return
        }
        for (const [v, val] of adj.get(src) || []) {
            dfs(adj, v, dst, visited, product * val, ans)
        }
    }
    const adj = new Map()
    for (let i = 0; i < equations.length; i++) {
        const u = equations[i][0]
        const v = equations[i][1]
        const val = values[i]
        if (!adj.has(u)) adj.set(u, [])
        if (!adj.has(v)) adj.set(v, [])
        adj.get(u).push([v, val])
        adj.get(v).push([u, 1.0 / val])
    }
    const result = []
    for (const query of queries) {
        const src = query[0]
        const dst = query[1]
        let ans = { value: -1.0 }
        const product = 1.0
        if (adj.has(src)) {
            const visited = new Set()
            dfs(adj, src, dst, visited, product, ans)
        }
        result.push(ans.value)
    }
    return result
};