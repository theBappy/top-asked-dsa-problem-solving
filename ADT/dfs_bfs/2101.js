
//DFS

var maximumDetonation = function (bombs) {
    const DFS = (u, visited, adj) => {
        visited.add(u)
        for (const v of (adj.get(u) || [])) {
            if (!visited.has(v)) {
                DFS(v, visited, adj)
            }
        }
    }
    const n = bombs.length
    const adj = new Map()
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (i === j) continue
            const x1 = bombs[i][0]
            const y1 = bombs[i][1]
            const r1 = bombs[i][2]

            const x2 = bombs[j][0]
            const y2 = bombs[j][1]
            const r2 = bombs[j][2]

            const distance = (x2 - x1) ** 2 + (y2 - y1) ** 2

            if (r1 * r1 >= distance) {
                if (!adj.has(i)) adj.set(i, [])
                adj.get(i).push(j)
            }
        }
    }
    let result = 0
    const visited = new Set()
    for (let i = 0; i < n; i++) {
        visited.clear()
        DFS(i, visited, adj)
        result = Math.max(result, visited.size)
    }
    return result
};


// BFS

var maximumDetonation = function (bombs) {
    const BFS = (u, adj) => {
        const visited = new Set()
        const queue = []
        queue.push(u)
        visited.add(u)
        while (queue.length > 0) {
            const temp = queue.shift()
            for (const v of (adj.get(temp) || [])) {
                if (!visited.has(v)) {
                    queue.push(v)
                    visited.add(v)
                }
            }
        }
        return visited.size
    }
    const n = bombs.length
    const adj = new Map()
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (i === j) continue
            const x1 = bombs[i][0]
            const y1 = bombs[i][1]
            const r1 = bombs[i][2]

            const x2 = bombs[j][0]
            const y2 = bombs[j][1]
            const r2 = bombs[j][2]

            const distance = (x2 - x1) ** 2 + (y2 - y1) ** 2

            if (r1 * r1 >= distance) {
                if (!adj.has(i)) adj.set(i, [])
                adj.get(i).push(j)
            }
        }
    }
    let result = 0
    for (let i = 0; i < n; i++) {
        const count = BFS(i, adj)
        if (count > result) result = count
    }
    return result
};