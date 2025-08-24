//Approach-1 (Recur + Memo) - It's Just Like coin change-2 (Only in this qn, assume that coin has k faces having different values)
//T.C : O(n*target*k) (But without memoization - it will be O(k^n)
//S.C : O(31*1001) ~= O(1)

class Solution {
public:
    int M = 1e9 + 7;
    int t[31][1001];
    int solve(int n, int k , int target){
        if(target < 0)
            return 0;
        if(n == 0)
            return target == 0;
        if(t[n][target] != -1)
            return t[n][target];
        int ways = 0;
        for(int face = 1; face <= k ; face++){
            ways = (ways + solve(n-1, k, target-face)) % M;
        }
        return t[n][target] = ways;
    }
    int numRollsToTarget(int n, int k, int target) {
        memset(t, -1, sizeof(t));
        return solve(n, k, target);
    }
};

// Bottom Up
class Solution {
public:
    int M = 1e9 + 7;
    int numRollsToTarget(int n, int k, int target) {
       vector<vector<int>> t(n+1, vector<int>(target+1));
        t[0][0] = 1; // n == 0 && target == 0
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= target; j++) {
                // i = number of dice
                // j = target value
                int ways = 0;
                for (int face = 1; face <= k; face++) {
                    if(face <= j){
                        ways = (ways + t[i - 1][j - face]) % M;
                    }
                }
            t[i][j] = ways;
            }
        }
        return t[n][target];
    }
};