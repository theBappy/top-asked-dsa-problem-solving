/**
 * @param {number[][]} matrix
 * @return {number}
 */
var maxMatrixSum = function (matrix) {
    const n = matrix.length
    let sum = 0
    let countNegatives = 0
    let smallestAbsValue = Number.MAX_SAFE_INTEGER
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            const val = matrix[i][j]
            const absVal = Math.abs(val)
            sum += absVal
            if (val < 0) countNegatives++
            if (absVal < smallestAbsValue) {
                smallestAbsValue = absVal
            }
        }
    }
    if (countNegatives % 2 === 0) {
        return sum
    }
    return sum - 2 * smallestAbsValue
};