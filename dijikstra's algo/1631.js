

class Solution {
    minimumEffortPath(heights) {
        const m = heights.length, n = heights[0].length;

        const isSafe = (x, y) => 0 <= x && x < m && 0 <= y && y < n;

        const result = Array.from({ length: m }, () => Array(n).fill(Infinity));
        const pq = [];

        pq.push([0, [0, 0]]);
        result[0][0] = 0;

        const directions = [[-1, 0], [0, -1], [0, 1], [1, 0]];

        while (pq.length) {
            const [diff, [x, y]] = pq.shift();

            if (x === m - 1 && y === n - 1) {
                return diff;
            }

            for (const dir of directions) {
                const x_ = x + dir[0], y_ = y + dir[1];

                if (isSafe(x_, y_)) {
                    const newDiff = Math.max(diff, Math.abs(heights[x][y] - heights[x_][y_]));
                    if (result[x_][y_] > newDiff) {
                        result[x_][y_] = newDiff;
                        pq.push([result[x_][y_], [x_, y_]]);
                    }
                }
            }
        }

        return result[m - 1][n - 1];
    }
}