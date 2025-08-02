/**
 * @param {string[][]} maze
 * @param {number[]} entrance
 * @return {number}
 */
var nearestExit = function(maze, entrance) {
    const m = maze.length;
    const n = maze[0].length;
    
    // A queue for BFS. Each element is an array [row, col, steps].
    const queue = [[entrance[0], entrance[1], 0]];
    
    // Mark the entrance as a wall to prevent revisiting.
    // Using a different character like 'v' for visited can also work,
    // but '+' is a valid choice since walls are not traversable anyway.
    maze[entrance[0]][entrance[1]] = '+';
    
    // Define the 4 possible directions for movement.
    const directions = [
        [0, 1],  // Right
        [0, -1], // Left
        [1, 0],  // Down
        [-1, 0]  // Up
    ];
    
    let head = 0; // Pointer to the head of the queue (using array as a queue)
    
    // Continue the BFS as long as the queue is not empty.
    while (head < queue.length) {
        const [i, j, steps] = queue[head++];
        
        // Check for an exit condition. An exit is any cell on the border
        // that is not the entrance itself.
        // `steps > 0` ensures we don't count the entrance as an exit.
        if (steps > 0 && (i === 0 || i === m - 1 || j === 0 || j === n - 1)) {
            return steps;
        }
        
        // Explore the neighbors.
        for (const [dx, dy] of directions) {
            const newI = i + dx;
            const newJ = j + dy;
            
            // Check if the new cell is within the maze boundaries.
            if (newI >= 0 && newI < m && newJ >= 0 && newJ < n) {
                // Check if the new cell is an empty path ('.').
                if (maze[newI][newJ] === '.') {
                    // Mark the new cell as visited by changing it to a wall.
                    maze[newI][newJ] = '+';
                    // Add the new cell and the incremented step count to the queue.
                    queue.push([newI, newJ, steps + 1]);
                }
            }
        }
    }
    
    // If the loop finishes without finding an exit, no path exists.
    return -1;
};