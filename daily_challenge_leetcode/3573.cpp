
//Approach-1 (Recursion + Memoization)
//T.C : O(n * k)
//S.C : O(n * k)
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // DP table: t[i][k][CASE]
    // i -> current day index
    // k -> remaining transactions
    // CASE -> 0: can buy/sell, 1: must buy, 2: must sell
    long long t[1001][501][3];
    const long long INF = 1e18; // safe sentinel to avoid overflow

    // Recursive DP function
    long long solve(int i, int k, int CASE, vector<int>& prices) {
        int n = prices.size();

        // Base case: if we reach the end of prices array
        if (i == n) {
            if (CASE == 0) return 0;       // no pending action, profit = 0
            return -INF;                   // invalid state, return negative infinity
        }

        // Check if this state is already computed
        if (t[i][k][CASE] != -INF)
            return t[i][k][CASE];

        long long take = -INF; // profit if we take an action
        long long skip = solve(i + 1, k, CASE, prices); // profit if we skip today

        if (k > 0) {
            if (CASE == 1) {
                // CASE 1: must sell today
                take = prices[i] + solve(i + 1, k - 1, 0, prices);
            }
            else if (CASE == 2) {
                // CASE 2: must buy today
                take = -prices[i] + solve(i + 1, k - 1, 0, prices);
            }
            else {
                // CASE 0: can choose to buy or sell
                take = max(
                    -prices[i] + solve(i + 1, k, 1, prices), // buy today
                    prices[i] + solve(i + 1, k, 2, prices)   // sell today
                );
            }
        }

        // Save and return the maximum of taking or skipping
        return t[i][k][CASE] = max(take, skip);
    }

    long long maximumProfit(vector<int>& prices, int k) {
        int n = prices.size();

        // Initialize DP table with sentinel
        for (int i = 0; i < n; i++)
            for (int j = 0; j <= k; j++)
                for (int l = 0; l < 3; l++)
                    t[i][j][l] = -INF;

        // Start recursion from day 0, with k transactions left, and CASE 0 (can buy/sell)
        return solve(0, k, 0, prices);
    }
};

// Example usage:
// int main() {
//     Solution sol;
//     vector<int> prices = {3,2,6,5,0,3};
//     int k = 2;
//     cout << sol.maximumProfit(prices, k) << endl; // Output: maximum profit
//     return 0;
// }
