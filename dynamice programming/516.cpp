// Google, Linkedin, Amazon, PayPal, Uber
// Tc = O(m.n)
// Sc = O(m.n)

// Approach-1
class Solution {
public:
    // recursion + memo
    int t[1001][1001];
    
    int LCS(string& s1, string& s2, int m, int n) {
        if (n == 0 || m == 0)
            return t[m][n] = 0;
        if (t[m][n] != -1)
            return t[m][n];
        if (s1[m - 1] == s2[n - 1])
            return t[m][n] = 1 + LCS(s1, s2, m - 1, n - 1);

        return t[m][n] = max(LCS(s1, s2, m, n - 1), LCS(s1, s2, m - 1, n));
    }
    
    int longestPalindromeSubseq(string s1) {
        memset(t, -1, sizeof(t));
        string s2 = s1;
        reverse(begin(s2), end(s2));
        int m = s1.length();
        return LCS(s1, s2, m, m);
    }
};


// Tc = O(m.n)
// Sc = O(m.n)
//Approach-2
class Solution {
public:
    int t[1001][1001];
    int solve(string& s, int i, int j){
        if(i > j)
            return 0;
        if(i == j)
            return 1;
        if(t[i][j] != -1)
            return t[i][j];
        if(s[i] == s[j])
            return t[i][j] = 2 + solve(s, i+1, j-1);
        else 
            return t[i][j] = max(solve(s, i+1, j), solve(s, i, j-1));
    }
    int longestPalindromeSubseq(string s) {
        memset(t, -1, sizeof(t));
        return solve(s, 0, s.length() -1);
    }
};
