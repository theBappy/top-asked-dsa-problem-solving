
var countPermutations = function (complexity) {
    const M = 1e9 + 7
    const n = complexity.length
    let result = 1
    for (let i = 1; i < n; i++) {
        if (complexity[i] <= complexity[0]) {
            return 0
        }
        result = (result * i) % M
    }
    return result
};