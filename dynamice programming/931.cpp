class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int n = matrix.size();
        vector<vector<int>> t(n, vector<int>(n));
        for(int col = 0; col < n ; col++){
            t[0][col] = matrix[0][col];
        }
        for(int row = 1; row < n; row++){
            for(int col = 0; col < n; col++){
                int a = INT_MAX;
                int b = INT_MAX;
                int c  = INT_MAX;
                if(col-1 >= 0)
                    a = t[row-1][col-1];
                if(col + 1 < n)
                    b = t[row-1][col+1];
                t[row][col] = matrix[row][col] +  min({t[row-1][col],a,b});
            }
        }
        int result = INT_MAX;
        int lastRow = n - 1;
        for(int col = 0; col < n; col++){
            result = min(result, t[lastRow][col]);
        }
        return result;
    }
};


// decrease line
class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int n = matrix.size();
        for (int row = n-2; row >= 0; row--) {
            for (int col = 0; col < n; col++) {
                int best = matrix[row+1][col];
                if (col > 0) best = min(best, matrix[row+1][col-1]);
                if (col+1 < n) best = min(best, matrix[row+1][col+1]);
                matrix[row][col] += best;
            }
        }
        return *min_element(matrix[0].begin(), matrix[0].end());
    }
};