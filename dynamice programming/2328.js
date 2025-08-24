

function countPaths(grid){
    const m = grid.length, n = grid[0].length;
    const MOD = 10**9 + 7;
    const directions = [[-1, 0], [0, -1], [0, 1], [1, 0]];
    const t = Array.from({ length: m }, () => Array(n).fill(-1));

    function isSafe(i, j) {
        return 0 <= i && i < m && 0 <= j && j < n;
    }

    function dfs(i, j) {
        if (t[i][j] !== -1) {
            return t[i][j];
        }
        
        let answer = 1;  // Count the current cell
        for (const dir of directions) {
            const i_ = i + dir[0], j_ = j + dir[1];
            if (isSafe(i_, j_) && grid[i_][j_] < grid[i][j]) {
                answer = (answer + dfs(i_, j_)) % MOD;
            }
        }
        
        t[i][j] = answer;
        return answer;
    }

    let result = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            result = (result + dfs(i, j)) % MOD;
        }
    }
    
    return result;
}