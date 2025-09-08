/**
 * @param {number} n
 * @param {number[][]} queries
 * @return {number[]}
 */
var productQueries = function (n, queries) {
    const M = 1e9 + 7
    const powers = []
    const result = []
    for (let i = 0; i < 32; i++) {
        if ((n & (1 << i)) !== 0) {
            powers.push(1 << i)
        }
    }
    for (const query of queries) {
        const start = query[0]
        const end = query[1]
        let product = 1
        for (let i = start; i <= end; i++) {
            product = (product * powers[i]) % M
        }
        result.push(product)
    }
    return result
};