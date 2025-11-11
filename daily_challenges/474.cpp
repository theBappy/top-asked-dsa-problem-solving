
// Why Greedy fails?(by sorting)
// 0/1 knap-snack will work

//Approach-1 (Recursion and Memoization)
// T.C : O(L * m * n)
//       where L = number of strings, m = max number of 0's allowed, n = max number of 1's allowed
//       For each index (L), we compute at most m*n states once due to memoization.
// S.C : O(L * m * n) for the DP cache + O(L) recursion stack

class Solution {
public:
    int t[101][101][601];
    int solve(vector<pair<int, int>>& count, int m, int n, int index) {
        if(index >= count.size() || (m == 0 && n == 0))
            return 0;
        if(t[m][n][index] != -1)
            return t[m][n][index];
        
        int include = 0;
        if(count[index].first <= m && count[index].second <= n) {
            include = 1 + solve(count, m-count[index].first, n-count[index].second, index+1);
        }
        
        int exclude = solve(count, m, n, index+1);
        
        return t[m][n][index] = max(include, exclude);
    }
    int findMaxForm(vector<string>& strs, int m, int n) {
        int N = strs.size();
        vector<pair<int, int>> count(N);
        int i = 0;\
        for(string str:strs) {
            int countOnes  = 0;
            int countZeros = 0;
            
            for(char ch:str) {
                if(ch == '1')
                    countOnes++;
                else
                    countZeros++;
            }
            
            count[i++] = {countZeros, countOnes};
        }
        
        memset(t, -1, sizeof(t));
        return solve(count, m, n, 0);
    }
};