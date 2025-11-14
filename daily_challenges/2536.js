/**
 * @param {number} n
 * @param {number[][]} queries
 * @return {number[][]}
 */
var rangeAddQueries = function (n, queries) {
    const diff = Array.from({ length: n }, () => Array(n).fill(0));

    for (const query of queries) {
        const [row1, col1, row2, col2] = query;

        for (let i = row1; i <= row2; i++) {
            diff[i][col1] += 1;

            if (col2 + 1 < n)
                diff[i][col2 + 1] -= 1;
        }
    }
    for (let i = 0; i < n; i++) {
        for (let j = 1; j < n; j++) {
            diff[i][j] += diff[i][j - 1];
        }
    }

    return diff;
};