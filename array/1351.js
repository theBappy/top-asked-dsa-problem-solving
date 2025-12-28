
/**
 * @param {number[][]} grid
 * @return {number}
 */
var countNegatives = function (grid) {
    const m = grid.length;
    const n = grid[0].length;

    let result = 0;

    for (const row of grid) {
        // upper_bound equivalent: find first element <= 0 in descending sorted array
        let left = 0, right = n;
        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (row[mid] >= 0) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        const idx = left;
        result += n - idx;
    }

    return result;
};

/**
 * @param {number[][]} grid
 * @return {number}
 */
var countNegatives = function (grid) {
    const m = grid.length
    const n = grid[0].length
    let row = m - 1
    let col = 0
    let result = 0
    while (row >= 0 && col < n) {
        if (grid[row][col] < 0) {
            result += n - col
            row -= 1
        } else {
            col += 1
        }
    }
    return result
};