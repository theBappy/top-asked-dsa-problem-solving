/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function (triangle) {
    const n = triangle.length;

    for (let row = 1; row < n; row++) {
        for (let col = 0; col < triangle[row].length; col++) {
            // take value directly above (or clamp to last element if col is out of range)
            const prev_up = triangle[row - 1][Math.min(col, triangle[row - 1].length - 1)];
            // take value from above-left (or clamp to 0 if col-1 < 0)
            const prev_left = triangle[row - 1][Math.max(col - 1, 0)];

            // update DP in place
            triangle[row][col] += Math.min(prev_up, prev_left);
        }
    }

    // minimum path sum is the smallest element in the last row
    return Math.min(...triangle[n - 1]);
};
