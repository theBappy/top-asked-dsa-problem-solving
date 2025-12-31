// Google, Meta

// DFS + Binary Search
// TC = O{(row * col) * logn} [logn for binary search]
class Solution {
public:
    int ROW;
    int COL;
    vector<vector<int>> directions{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    bool DFS(vector<vector<int>>& grid, int i, int j) {
        if (i < 0 || i >= ROW || j < 0 || j >= COL || grid[i][j] == 1) {
            return false;
        }
        if (i == ROW - 1) {
            return true;
        }
        grid[i][j] = 1;
        for (vector<int>& dir : directions) {
            int new_i = i + dir[0];
            int new_j = j + dir[1];
            if (DFS(grid, new_i, new_j))
                return true;
        }
        return false;
    }
    bool canCross(vector<vector<int>>& cells, int mid) {
        vector<vector<int>> grid(ROW, vector<int>(COL));
        for (int i = 0; i <= mid; i++) {
            int x = cells[i][0] - 1;
            int y = cells[i][1] - 1;
            grid[x][y] = 1;
        }
        for (int j = 0; j < COL; j++) {
            if (grid[0][j] == 0 && DFS(grid, 0, j)) {
                return true;
            }
        }
        return false;
    }
    int latestDayToCross(int row, int col, vector<vector<int>>& cells) {
        ROW = row;
        COL = col;
        int l = 0;
        int r = cells.size() - 1;
        int lastDay = 0;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (canCross(cells, mid)) {
                lastDay = mid + 1;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return lastDay;
    }
};



// BFS + Binary Search
class Solution {
public:
    int ROW;
    int COL;
    vector<vector<int>> directions{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    bool BFS(vector<vector<int>>& grid, int i, int j) {
        queue<pair<int, int>> que;
        que.push({i, j});
        grid[i][j] = 1;
        while (!que.empty()) {
            auto temp = que.front();
            que.pop();
            int x = temp.first;
            int y = temp.second;
            if (x == ROW - 1)
                return true;
            for (vector<int>& dir : directions) {
                int new_x = x + dir[0];
                int new_y = y + dir[1];
                if (new_x >= 0 && new_x < ROW && new_y >= 0 && new_y < COL &&
                    grid[new_x][new_y] == 0) {
                    que.push({new_x, new_y});
                    grid[new_x][new_y] = true;
                }
            }
        }
        return false;
    }
    bool canCross(vector<vector<int>>& cells, int mid) {
        vector<vector<int>> grid(ROW, vector<int>(COL));
        for (int i = 0; i <= mid; i++) {
            int x = cells[i][0] - 1;
            int y = cells[i][1] - 1;
            grid[x][y] = 1;
        }
        for (int j = 0; j < COL; j++) {
            if (grid[0][j] == 0 && BFS(grid, 0, j)) {
                return true;
            }
        }
        return false;
    }
    int latestDayToCross(int row, int col, vector<vector<int>>& cells) {
        ROW = row;
        COL = col;
        int l = 0;
        int r = cells.size() - 1;
        int lastDay = 0;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (canCross(cells, mid)) {
                lastDay = mid + 1;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return lastDay;
    }
};