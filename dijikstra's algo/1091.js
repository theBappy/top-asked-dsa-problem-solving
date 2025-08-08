class Solution {
    shortestPathBinaryMatrix(grid) {
        const m = grid.length, n = grid[0].length;
        if (m === 0 || n === 0 || grid[0][0] !== 0) {
            return -1;
        }

        const directions = [[1, 1], [0, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [1, -1], [-1, 1]];
        
        const isSafe = (x, y) => 0 <= x && x < m && 0 <= y && y < n;
        
        const result = Array.from({ length: m }, () => Array(n).fill(Infinity));
        const pq = [];

        pq.push([0, 0, 0]);  // (distance, x, y)
        result[0][0] = 0;
        
        while (pq.length > 0) {
            const [d, x, y] = pq.shift();
            
            for (const [dx, dy] of directions) {
                const x_ = x + dx;
                const y_ = y + dy;
                const dist = 1;

                if (isSafe(x_, y_) && grid[x_][y_] === 0 && d + dist < result[x_][y_]) {
                    pq.push([d + dist, x_, y_]);
                    grid[x_][y_] = 1;  // mark as visited
                    result[x_][y_] = d + dist;
                }
            }
        }
        
        if (result[m - 1][n - 1] === Infinity) {
            return -1;
        }
        
        return result[m - 1][n - 1] + 1;
    }
}