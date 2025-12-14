// Google, Meta, Microsoft, Amazon

// Using BFS

/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestPathBinaryMatrix = function (grid) {
    const directions = [
        [1, 1], [0, 1], [1, 0], [0, -1],
        [-1, 0], [-1, -1], [1, -1], [-1, 1]
    ];
    const m = grid.length;
    const n = grid[0].length;
    if (m === 0 || n === 0 || grid[0][0] !== 0) return -1;

    const queue = [];
    queue.push([0, 0]);
    grid[0][0] = 1;

    const isSafe = (x, y) => x >= 0 && x < m && y >= 0 && y < n;

    let steps = 1;

    while (queue.length > 0) {
        let N = queue.length;
        while (N--) {
            const [x, y] = queue.shift();

            if (x === m - 1 && y === n - 1) return steps;

            for (const dir of directions) {
                const x_ = x + dir[0];
                const y_ = y + dir[1];

                if (isSafe(x_, y_) && grid[x_][y_] === 0) {
                    queue.push([x_, y_]);
                    grid[x_][y_] = 1;
                }
            }
        }
        steps++;
    }

    return -1;
};