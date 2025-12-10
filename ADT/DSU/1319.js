/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number}
 */
var makeConnected = function (n, connections) {
    const parent = new Array(n).fill(0).map((_, i) => i)
    const rank = new Array(n).fill(1)

    const find = (x) => {
        if (parent[x] !== x) {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }

    const Union = (x, y) => {
        const px = find(x)
        const py = find(y)
        if (px !== py) {
            if (rank[px] > rank[py]) {
                parent[py] = px
            } else if (rank[px] < rank[py]) {
                parent[px] = py
            } else {
                parent[px] = py
                rank[py] += 1
            }
        }
    }

    if (connections.length < n - 1) {
        return -1
    }
    let components = n
    for (const vec of connections) {
        if (find(vec[0]) !== find(vec[1])) {
            components--
            Union(vec[0], vec[1])
        }
    }
    return components - 1
};