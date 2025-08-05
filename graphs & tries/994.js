class Solution {
    orangesRotting(grid) {
        let fresh = 0;
        let rotten = [];
        let minutes = 0;
        const rows = grid.length, cols = grid[0].length;

        for (let row = 0; row < rows; row++) {
            for (let col = 0; col < cols; col++) {
                if (grid[row][col] === 1) {
                    fresh++;
                } else if (grid[row][col] === 2) {
                    rotten.push([row, col]);
                }
            }
        }

        while (rotten.length > 0 && fresh > 0) {
            minutes++;
            let curr = [];
            for (let [r, c] of rotten) {
                const check = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]];
                for (let [i, j] of check) {
                    if (i >= 0 && j >= 0 && i < rows && j < cols && grid[i][j] === 1) {
                        grid[i][j] = 2;
                        fresh--;
                        curr.push([i, j]);
                        if (fresh === 0) {
                            return minutes;
                        }
                    }
                }
            }
            rotten = curr;
        }

        return fresh === 0 ? minutes : -1;
    }
}