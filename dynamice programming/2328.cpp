class Solution {
public:
    int m, n;
    vector<vector<int>> directions = {
                {-1,0},
        {0,-1},         {0,1},
                {1, 0}
    };
    
    bool isSafe(int i, int j) {
        return (i < m && i >= 0 && j < n && j >= 0);
    }
    
    long long MOD = 1e9+7;
    int t[1001][1001];
    
    int dfs(vector<vector<int>>& grid, int i, int j) {
        
        int answer = 1;
        if(t[i][j] != -1){
            return t[i][j];
        }
        
        for(auto &dir : directions) {
            int i_ = i + dir[0];
            int j_ = j + dir[1];
            
            if(isSafe(i_, j_) && grid[i_][j_] < grid[i][j]) {
                answer = (answer + dfs(grid, i_, j_)) % MOD;
            }
        }
        
        return t[i][j] = answer;
        
    }
    
    int countPaths(vector<vector<int>>& grid) {
        m = grid.size();
        n = grid[0].size();
        
        memset(t, -1, sizeof(t));
        int result = 0;
        
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                
                result = (result + dfs(grid, i, j)) % MOD;
                
            }
        }
        
        
        return result;
    }
};