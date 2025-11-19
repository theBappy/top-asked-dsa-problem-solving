// Recursion + Memoization
// Tc & Sc = O(n^2)
// gave TLE 
class Solution {
public:
    int n;
    int t[201][201];
    int solve(vector<vector<int>>& triangle, int row, int col) {
        if (row == n - 1) {
            return triangle[row][col];
        }
        if(t[row][col] != -1){
            return t[row][col];
        }
        int minPathSum =
            triangle[row][col] + min(solve(triangle, row + 1, col),
                                     solve(triangle, row + 1, col + 1));
        t[row][col] = minPathSum;
        return t[row][col];                        
    }
    int minimumTotal(vector<vector<int>>& triangle) {
        n = triangle.size();
        memset(t, -1, sizeof(t));

        return solve(triangle, 0, 0);
    }
};

// Bottom-up
// State define: t[row][col] => min path sum from [row][col] to bottom of the triangle
// Tc=O(n^2) and Sc = O(n^2)
// but it will pass
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        vector<vector<int>> t = triangle;
        for (int row = n - 2; row >= 0; row--) {
            for (int col = 0; col <= row; col++) {
                t[row][col] =
                    t[row][col] + min(t[row + 1][col], t[row + 1][col + 1]);
            }
        }
        return t[0][0];
    }
};

// optimizing bottom up
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        vector<int> t = triangle[n-1];
        for (int row = n - 2; row >= 0; row--) {
            for (int col = 0; col <= row; col++) {
                t[col] =
                    triangle[row][col] + min(t[col], t[col + 1]);
            }
        }
        return t[0];
    }
};


// Approach-4
//T.C : O(n^2)
//S.C : O(1)
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        
        for(int row = 1; row < n; row++) {
            for(int col = 0; col<triangle[row].size(); col++) {
                int prev_up_val  = triangle[row-1][min(col, (int)triangle[row-1].size()-1)];
                int prev_up_left = triangle[row-1][max(col-1, 0)];
                
                triangle[row][col] += min(prev_up_val, prev_up_left);
            }
        }
        return *min_element(triangle[n-1].begin(), triangle[n-1].end());
    }
};