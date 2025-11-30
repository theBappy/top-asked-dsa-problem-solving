
var minMutation = function (start, end, bank) {
    const bankset = new Set(bank)
    const visited = new Set()
    const q = []
    q.push(start)
    visited.add(start)
    let level = 0
    while (q.length > 0) {
        let n = q.length
        while (n--) {
            const curr = q.shift()
            if (curr === end)
                return level
            for (const ch of "ACGT") {
                for (let i = 0; i < curr.length; i++) {
                    const neighbor = curr.slice(0, i) + ch + curr.slice(i + 1)
                    if (!visited.has(neighbor) && bankset.has(neighbor)) {
                        visited.add(neighbor)
                        q.push(neighbor)
                    }
                }
            }
        }
        level++
    }
    return -1
};