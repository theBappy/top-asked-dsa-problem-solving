// Google

// Brute Force
//T.C : O(m*n)
//S.C : O(1)

class Solution {
public:

    bool isMagicGrid(vector<vector<int>>& grid, int r, int c) {
        //uniqueness 1 to 9 and distinct
        unordered_set<int> st;
        for(int i = 0; i < 3; i++) {
            for(int j = 0; j < 3; j++) {
                int num = grid[r+i][c+j];
                if(num < 1 || num > 9 || st.count(num)) {
                    return false;
                } else {
                    st.insert(num);
                }
            }
        }

        //check Sum - Rows and columns
        int SUM = grid[r][c] + grid[r][c+1] + grid[r][c+2];
        for(int i = 0; i < 3; i++) {
            if(grid[r+i][c] + grid[r+i][c+1] + grid[r+i][c+2] != SUM) {
                return false;
            }

            if(grid[r][c+i] + grid[r+1][c+i] + grid[r+2][c+i] != SUM) {
                return false;
            }
        }


        //diaornal and anti-diagonal
        if(grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != SUM) {
            return false;
        }

        if(grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != SUM) {
            return false;
        }
        

        return true;


    }

    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();

        int count = 0;

        for(int i = 0; i <= rows-3; i++) {
            for(int j = 0; j <= cols-3; j++) {
                if(isMagicGrid(grid, i, j)) {
                    count++;
                }
            }
        }

        return count;
    }
};
