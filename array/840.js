/**
 * @param {number[][]} grid
 * @return {number}
 */
var numMagicSquaresInside = function (grid) {
    const isMagicGrid = (r, c) => {
        const st = new Set();
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                const num = grid[r + i][c + j];
                if (num < 1 || num > 9 || st.has(num)) {
                    return false;
                } else {
                    st.add(num);
                }
            }
        }

        // check Sum - Rows and columns
        const SUM = grid[r][c] + grid[r][c + 1] + grid[r][c + 2];
        for (let i = 0; i < 3; i++) {
            if (grid[r + i][c] + grid[r + i][c + 1] + grid[r + i][c + 2] !== SUM) {
                return false;
            }

            if (grid[r][c + i] + grid[r + 1][c + i] + grid[r + 2][c + i] !== SUM) {
                return false;
            }
        }

        // diagonal and anti-diagonal
        if (grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] !== SUM) {
            return false;
        }

        if (grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] !== SUM) {
            return false;
        }

        return true;
    }
    const rows = grid.length;
    const cols = grid[0].length;
    let count = 0;

    for (let i = 0; i <= rows - 3; i++) {
        for (let j = 0; j <= cols - 3; j++) {
            if (isMagicGrid(i, j)) {
                count++;
            }
        }
    }

    return count;
};