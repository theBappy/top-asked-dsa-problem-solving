/**
 * @param {number[]} prices
 * @param {number} k
 * @return {number}
 */
var maximumProfit = function (prices, k) {
    const n = prices.length
    const INF = 1e18

    const dp = Array.from({length: n}, () => 
        Array.from({length: k+1}, () => Array(3).fill(-INF))
    );

    const solve = (i, k_remain, CASE) => {
        // Base case: reached end of array
        if (i === n) {
            if (CASE === 0) return 0;
            return -INF;
        }

        // Memoization check
        if (dp[i][k_remain][CASE] !== -INF) return dp[i][k_remain][CASE];

        // Skip today
        let skip = solve(i + 1, k_remain, CASE);
        let take = -INF;

        if (k_remain > 0) {
            if (CASE === 1) {
                // Must sell today
                take = prices[i] + solve(i + 1, k_remain - 1, 0);
            } else if (CASE === 2) {
                // Must buy today
                take = -prices[i] + solve(i + 1, k_remain - 1, 0);
            } else {
                // Can choose to buy or sell
                take = Math.max(
                    -prices[i] + solve(i + 1, k_remain, 1), // buy
                    prices[i] + solve(i + 1, k_remain, 2)   // sell
                );
            }
        }
        dp[i][k_remain][CASE] = Math.max(skip, take);
        return dp[i][k_remain][CASE];
    };

    return solve(0, k, 0);
};