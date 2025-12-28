// Amazon

// Brute Force - O(m * n)
// m = rows
// n = columns
class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        int result = 0;
        
        for(int i = 0; i<m; i++) {
            for(int j = 0; j<n; j++) {
                
                if(grid[i][j] < 0)
                    result++;
                
            }
        }
        
        return result;
    }
};


// By finding first negative element in a non-decreasing array
// Using Binary Search - upper_bound - SLIGHT OPTIMAL - O(m * log(n)) [Binary search for upper bound technique]
class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        int result = 0;

        for (auto& row : grid) {

            int idx = upper_bound(begin(row), end(row), 0, greater<int>()) -
                      begin(row);

            result += n - idx;
        }

        return result;
    }
};

// Using the sorted proprrty - O(m+n)
// Why m + n ???
// O(row) + O(col) => when find one positive integeger discarding a column bkz it's above will be greater positive as it is non-decreasing fashion in row and column wise
class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int row = m - 1;
        int col = 0;
        int result = 0;
        while (row >= 0 && col < n) {
            if (grid[row][col] < 0) {
                result += n - col;
                row--;
            } else {
                col++;
            }
        }
        return result;
    }
};