/**
 * @param {number} n
 * @param {number} x
 * @return {number}
 */
var numberOfWays = function (n, x) {
    const M = 1e9 + 7
    const t = Array.from({ length: 301 }, () => Array(301).fill(-1))

    const solve = (n, num, x) => {
        if(n == 0) {
            return 1
        }
        if(n < 0) {
            return 0
        }
        const currPowerVal = Math.pow(num, x)
        if (currPowerVal > n) {
            return 0
        }
        if (t[n][num] !== -1) {
            return t[n][num]
        }
        const take = solve(n - currPowerVal, num + 1, x)
        const skip = solve(n, num + 1, x)
        t[n][num] = (take + skip) % M
        return t[n][num]
    }
    return solve(n, 1, x)

};