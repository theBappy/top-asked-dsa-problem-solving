function minFallingPathSum(matrix) {
    const n = matrix.length;
    for (let row = n - 2; row >= 0; row--) {
        for (let col = 0; col < n; col++) {
            let best = matrix[row + 1][col];
            if (col > 0) {
                best = Math.min(best, matrix[row + 1][col - 1]);
            }
            if (col + 1 < n) {
                best = Math.min(best, matrix[row + 1][col + 1]);
            }
            matrix[row][col] += best;
        }
    }
    return Math.min(...matrix[0]);
}