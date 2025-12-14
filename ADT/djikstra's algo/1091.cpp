
// Using BFS
class Solution {
public:
    vector<vector<int>> directions{{1, 1},  {0, 1},   {1, 0},  {0, -1},
                                   {-1, 0}, {-1, -1}, {1, -1}, {-1, 1}};
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        if (m == 0 || n == 0 || grid[0][0] != 0)
            return -1;

        queue<pair<int, int>> que;
        que.push({0, 0});
        grid[0][0] = 1;

        auto isSafe = [&](int x, int y) {
            return x >= 0 && x < m && y >= 0 && y < n;
        };

        int steps = 1;

        while (!que.empty()) {

            int N = que.size();
            while (N--) {

                auto curr = que.front();
                que.pop();
                int x = curr.first;
                int y = curr.second;

                if (x == m - 1 && y == n - 1)
                    return steps;

                for (auto dir : directions) {
                    int x_ = x + dir[0];
                    int y_ = y + dir[1];

                    if (isSafe(x_, y_) && grid[x_][y_] == 0) {
                        que.push({x_, y_});
                        grid[x_][y_] = 1;
                    }
                }
            }
            steps++;
        }

        return -1;
    }
};

// Using Dijikstra's Algo
class Solution {
public:
    typedef pair<int, pair<int, int>> P;
    vector<vector<int>> directions{{1,1}, {0,1},{1,0},{0,-1},{-1,0},{-1, -1},{1, -1},{-1, 1}};
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        if(m == 0 || n == 0 || grid[0][0] != 0)
            return -1;

        auto isSafe = [&](int x, int y) {
            return x>=0 && x<m && y>=0 && y<n;
        };
        
        vector<vector<int>> result(m, vector<int>(n, INT_MAX));
        priority_queue<P, vector<P>, greater<P>> pq;
        
        pq.push({0, {0, 0}});
        result[0][0] = 0;
  
        while(!pq.empty()) {
            int d  = pq.top().first;
	    pair<int, int> node = pq.top().second;
	    pq.pop();

            int x = node.first;
            int y = node.second;
            
	    for(auto dir:directions) {
		int x_   = x + dir[0];
		int y_   = y + dir[1];
		int dist = 1;

		if(isSafe(x_, y_) && grid[x_][y_] == 0 && d+dist < result[x_][y_]) {
		    pq.push({d+dist, {x_, y_}});
		    grid[x_][y_] = 1;
		    result[x_][y_] = d + dist;
		}
            }
        }
        
        if(result[m-1][n-1] == INT_MAX)
            return -1;
        
        return result[m-1][n-1]+1;
        
    }
};
