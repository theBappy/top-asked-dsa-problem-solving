/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function (triangle) {
    const n = triangle.length
    for (let row = 1; row < n; row++) {
        for (let col = 0; col < triangle[row].length; col++) {
            const prev_up = triangle[row - 1][Math.min(col, triangle[row - 1].length - 1)]
            const prev_left = triangle[row - 1][Math.max(col - 1, 0)]
            triangle[row][col] += Math.min(prev_up, prev_left)
        }
    }
    return Math.min(...triangle[n - 1])
};