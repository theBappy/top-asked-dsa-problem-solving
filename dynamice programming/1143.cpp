// Top down(Recursion + Memoization)
class Solution {
public:
    int m, n;
    int t[1001][1001];
    int solve(string& s1, string& s2, int i, int j){
        if(i >= m || j >= n)
            return 0;
        if(t[i][j] != -1)
            return t[i][j];
        if(s1[i] == s2[j]){
            return t[i][j] = 1 + solve(s1,s2, i+1, j+1);
        }      
        return t[i][j] = max(solve(s1, s2, i, j+1), solve(s1, s2, i+1, j));
    }
    int longestCommonSubsequence(string s1, string s2) {
        m = s1.length();
        n = s2.length();
        memset(t, -1, sizeof(t));
        return solve(s1, s2, 0, 0);
    }
};

// Bottom Up
class Solution {
public:
    int longestCommonSubsequence(string s1, string s2) {
        int m = s1.length();
        int n = s2.length();
        vector<vector<int>> t(m+1, vector<int>(n+1));
        //first row and fist col will be -
        for(int row = 0; row < m+1; row++){
            t[row][0] = 0;
        }
        for(int col = 0; col < n+1; col++){
            t[0][col] = 0;
        }
        for(int i = 1; i<m+1; i++){
            for(int j = 1; j <n+1; j++){
                if(s1[i-1] == s2[j-1]){
                    t[i][j] = 1 + t[i-1][j-1];
                }else{
                    t[i][j] = max(t[i-1][j], t[i][j-1]);
                }
            }
        }
        return t[m][n];
    }
};