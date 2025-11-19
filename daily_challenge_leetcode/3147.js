/**
 * @param {number[]} energy
 * @param {number} k
 * @return {number}
 */
var maximumEnergy = function (energy, k) {
    const n = energy.length
    const dp = new Array(n).fill(0)
    let result = -Infinity
    for (let i = n - 1; i >= 0; i--) {
        dp[i] = energy[i] + ((i + k < n) ? dp[i + k] : 0)
        result = Math.max(result, dp[i])
    }
    return result
};