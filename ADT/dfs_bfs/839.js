var numSimilarGroups = function (strs) {
    const isSimilar = (s1, s2) => {
        let diff = 0
        for (let i = 0; i < s1.length; i++) {
            if (s1[i] !== s2[i]) diff++
        }
        return diff === 2 || diff === 0
    }

    const DFS = (u, adj, visited) => {
        visited[u] = true
        for (const v of adj.get(u) || []) {
            if (!visited[v]) DFS(v, adj, visited)
        }
    }

    const n = strs.length
    const adj = new Map()

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (isSimilar(strs[i], strs[j])) {
                if (!adj.has(i)) adj.set(i, [])
                if (!adj.has(j)) adj.set(j, [])
                adj.get(i).push(j)
                adj.get(j).push(i)
            }
        }
    }

    const visited = new Array(n).fill(false)
    let count = 0

    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            DFS(i, adj, visited)
            count++
        }
    }

    return count
}
