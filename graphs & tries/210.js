class Solution {
    dfs(grid, r, c) {
        grid[r][c] = '0';
        const lst = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]];
        for (const [row, col] of lst) {
            if (row >= 0 && col >= 0 && row < grid.length && col < grid[row].length && grid[row][col] === '1') {
                this.dfs(grid, row, col);
            }
        }
    }

    numIslands(grid) {
        let islands = 0;
        for (let r = 0; r < grid.length; r++) {
            for (let c = 0; c < grid[r].length; c++) {
                if (grid[r][c] === '1') {
                    this.dfs(grid, r, c);
                    islands += 1;
                }
            }
        }
        return islands;
    }
}