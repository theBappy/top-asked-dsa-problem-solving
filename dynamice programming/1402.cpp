// 0/1 knapsack
// Top Down(Recur+Memo)


class Solution {
public:
    int n;
    int dp[501][501];

    int solve(vector<int>& satisfaction, int i, int t){
        if(i >= n)
            return 0;
        if(dp[i][t] != -1)
            return dp[i][t];
        int include = satisfaction[i]*t + solve(satisfaction, i+1, t+1);
        int exclude = solve(satisfaction, i+1, t);
        return dp[i][t] = max(include, exclude);
    }
    int maxSatisfaction(vector<int>& satisfaction) {
        n = satisfaction.size();
        sort(begin(satisfaction), end(satisfaction));
        memset(dp, -1, sizeof(dp));
        return solve(satisfaction, 0, 1);
    }
};