// Maximum time in minimized path
// minimize the maximum
// maximum the minimum
// binary search on answer
// ans -> minimum time
//T.C : O(n^2 * log(n^2)) = O(n^2 log n)
//S.C : O(n^2) for visited
class Solution {
public:
    int n;
    vector<vector<int>> directions{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    bool visited[50][50];
    bool reachable(vector<vector<int>>& grid, int i, int j, int mid) {
        if(i < 0 || i >= n || j < 0 || j >= n || visited[i][j] || grid[i][j] > mid)
            return false;
        
        visited[i][j] = true;
        
        if(i == n-1 && j == n-1)
            return true;
        
        for(vector<int> &dir : directions) {
            int new_i = i + dir[0];
            int new_j = j + dir[1];
            
            if(reachable(grid, new_i, new_j, mid))
                return true;
        }
        
        return false;
    }
    
    int swimInWater(vector<vector<int>>& grid) {
        n = grid.size();
        
        int l = grid[0][0], r = n*n-1; //O(log(n^2))
        int result = 0;

        while(l <= r) {
            int mid = l + (r-l)/2;
            memset(visited, 0, sizeof(visited));
            
            if(reachable(grid, 0, 0, mid)) {
                result = mid;
                r = mid-1;
            } else {
                l = mid+1;
            }
        }
        
        return result;
    }
};