/**
 * @param {character[][]} maze
 * @param {number[]} entrance
 * @return {number}
 */
var nearestExit = function (maze, entrance) {
    const directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    const m = maze.length;
    const n = maze[0].length;

    const queue = [];
    queue.push([entrance[0], entrance[1]]);
    maze[entrance[0]][entrance[1]] = '+'; 
    let steps = 0;

    while (queue.length > 0) {
        let size = queue.length;

        while (size--) {
            const temp = queue.shift();

            if (!(temp[0] === entrance[0] && temp[1] === entrance[1]) &&
                (temp[0] === 0 || temp[0] === m - 1 || temp[1] === 0 || temp[1] === n - 1)) {
                return steps;
            }

            for (const dir of directions) {
                const i = temp[0] + dir[0];
                const j = temp[1] + dir[1];

                if (i >= 0 && i < m && j >= 0 && j < n && maze[i][j] !== '+') {
                    queue.push([i, j]);
                    maze[i][j] = '+'; 
                }
            }
        }
        steps++;
    }

    return -1;
};