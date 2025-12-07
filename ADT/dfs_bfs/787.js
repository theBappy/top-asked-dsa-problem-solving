/**
 * @param {number} n
 * @param {number[][]} flights
 * @param {number} src
 * @param {number} dst
 * @param {number} k
 * @return {number}
 */
var findCheapestPrice = function (n, flights, src, dst, k) {
    const distance = new Array(n).fill(Number.MAX_SAFE_INTEGER)
    const adj = new Map()
    for (const vec of flights) {
        const u = vec[0]
        const v = vec[1]
        const cost = vec[2]
        if (!adj.has(u)) adj.set(u, [])
        adj.get(u).push([v, cost])
    }
    const que = []
    que.push([src, 0])
    distance[src] = 0
    let level = 0
    while (que.length > 0 && level <= k) {
        const N = que.length
        for (let i = 0; i < N; i++) {
            const [u, d] = que.shift()
            if (!adj.has(u)) continue
            for (const [v, cost] of adj.get(u)) {
                if (distance[v] > d + cost) {
                    distance[v] = d + cost
                    que.push([v, d + cost])
                }
            }
        }
        level++
    }
    return distance[dst] === Number.MAX_SAFE_INTEGER ? -1 : distance[dst]
};