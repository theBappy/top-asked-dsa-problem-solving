// DFS + Bianry Search
/**
 * @param {number} row
 * @param {number} col
 * @param {number[][]} cells
 * @return {number}
 */
var latestDayToCross = function (row, col, cells) {
    const ROW = row;
    const COL = col;

    // Directions: down, up, right, left
    const directions = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1]
    ];

    function dfs(grid, i, j) {
        // Out of bounds or water or already visited
        if (i < 0 || i >= ROW || j < 0 || j >= COL || grid[i][j] === 1) {
            return false;
        }

        // Reached the last row
        if (i === ROW - 1) {
            return true;
        }

        // Mark cell as visited
        grid[i][j] = 1;

        // Explore all 4 directions
        for (const [dx, dy] of directions) {
            if (dfs(grid, i + dx, j + dy)) {
                return true;
            }
        }

        return false;
    }

    function canCross(mid) {
        // Initialize grid (0 = land, 1 = water)
        const grid = Array.from({ length: ROW }, () =>
            Array(COL).fill(0)
        );

        // Flood cells up to day 'mid'
        for (let i = 0; i <= mid; i++) {
            const x = cells[i][0] - 1;
            const y = cells[i][1] - 1;
            grid[x][y] = 1;
        }

        // Try to start DFS from every column in the top row
        for (let j = 0; j < COL; j++) {
            if (grid[0][j] === 0 && dfs(grid, 0, j)) {
                return true;
            }
        }

        return false;
    }

    // Binary search on days
    let left = 0;
    let right = cells.length - 1;
    let answer = 0;

    while (left <= right) {
        const mid = Math.floor(left + (right - left) / 2);

        if (canCross(mid)) {
            answer = mid + 1; // days are 1-based
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return answer;
};


// BFS + Binary Search
/**
 * @param {number} row
 * @param {number} col
 * @param {number[][]} cells
 * @return {number}
 */
var latestDayToCross = function (row, col, cells) {
    const ROW = row;
    const COL = col;

    const directions = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1]
    ];

    function bfs(grid, i, j) {
        let queue = [[i, j]];
        let head = 0;
        grid[i][j] = 1;

        while (head < queue.length) {
            let [x, y] = queue[head++];

            if (x === ROW - 1) return true;

            for (let [dx, dy] of directions) {
                let nx = x + dx;
                let ny = y + dy;

                if (
                    nx >= 0 && nx < ROW &&
                    ny >= 0 && ny < COL &&
                    grid[nx][ny] === 0
                ) {
                    grid[nx][ny] = 1;
                    queue.push([nx, ny]);
                }
            }
        }
        return false;
    }

    function canCross(mid) {
        // Initialize grid (0 = land, 1 = water)
        const grid = Array.from({ length: ROW }, () =>
            Array(COL).fill(0)
        );

        // Flood cells up to day 'mid'
        for (let i = 0; i <= mid; i++) {
            const x = cells[i][0] - 1;
            const y = cells[i][1] - 1;
            grid[x][y] = 1;
        }

        // Try to start bfs from every column in the top row
        for (let j = 0; j < COL; j++) {
            if (grid[0][j] === 0 && bfs(grid, 0, j)) {
                return true;
            }
        }

        return false;
    }

    // Binary search on days
    let left = 0;
    let right = cells.length - 1;
    let answer = 0;

    while (left <= right) {
        const mid = Math.floor(left + (right - left) / 2);

        if (canCross(mid)) {
            answer = mid + 1; // days are 1-based
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return answer;
};


// DSU
var latestDayToCross = function (row, col, cells) {
    const n = row * col;
    const TOP = n;
    const BOTTOM = n + 1;

    // DSU
    const parent = Array(n + 2).fill(0).map((_, i) => i);
    const rank = Array(n + 2).fill(0);

    function find(x) {
        if (parent[x] !== x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    function union(x, y) {
        let px = find(x);
        let py = find(y);
        if (px === py) return;

        if (rank[px] < rank[py]) parent[px] = py;
        else if (rank[px] > rank[py]) parent[py] = px;
        else {
            parent[py] = px;
            rank[px]++;
        }
    }

    const grid = Array.from({ length: row }, () =>
        Array(col).fill(0)
    );

    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];

    // Traverse days in reverse
    for (let day = cells.length - 1; day >= 0; day--) {
        const r = cells[day][0] - 1;
        const c = cells[day][1] - 1;
        grid[r][c] = 1;

        const id = r * col + c;

        // Connect to virtual nodes
        if (r === 0) union(id, TOP);
        if (r === row - 1) union(id, BOTTOM);

        // Union neighbors
        for (let [dr, dc] of dirs) {
            const nr = r + dr;
            const nc = c + dc;
            if (
                nr >= 0 && nr < row &&
                nc >= 0 && nc < col &&
                grid[nr][nc] === 1
            ) {
                union(id, nr * col + nc);
            }
        }

        // Check connectivity
        if (find(TOP) === find(BOTTOM)) {
            return day; // day is 0-based
        }
    }

    return 0;
};
