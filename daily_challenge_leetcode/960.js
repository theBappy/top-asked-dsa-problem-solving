/**
 * @param {string[]} strs
 * @return {number}
 */
var minDeletionSize = function (strs) {
    const rows = strs.length
    const cols = strs[0].length
    const dp = new Array(cols).fill(1)
    let LIS = 1
    for (let i = 0; i < cols; i++) {
        for (let j = 0; j < i; j++) {
            let valid = true
            for (let k = 0; k < rows; k++) {
                if (strs[k][j] > strs[k][i]) {
                    valid = false
                    break
                }
            }
            if (valid) {
                dp[i] = Math.max(dp[i], dp[j] + 1)
            }
        }
        LIS = Math.max(LIS, dp[i])
    }
    return cols - LIS
};