class Solution {
    removeStones(stones) {
        const n = stones.length;
        const visited = new Array(n).fill(false);
        let groups = 0;

        const dfs = (index) => {
            visited[index] = true;
            const [r, c] = stones[index];
            for (let i = 0; i < n; i++) {
                if (!visited[i] && (stones[i][0] === r || stones[i][1] === c)) {
                    dfs(i);
                }
            }
        };
        
        for (let i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i);
                groups++;
            }
        }
        return n - groups;
    }
}