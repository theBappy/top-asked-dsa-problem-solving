var maxSatisfaction = function (satisfaction) {
    const n = satisfaction.length;
    satisfaction.sort((a, b) => a - b);
    const dp = Array.from({ length: n + 1 }, () => Array(n + 1).fill(-1));
    
    const solve = (i, t) => {
        if (i >= n) {
            return 0;
        }
        if (dp[i][t] !== -1) { 
            return dp[i][t];
        }

        const include = satisfaction[i] * t + solve(i + 1, t + 1);
        const exclude = solve(i + 1, t);
        dp[i][t] = Math.max(include, exclude);
        return dp[i][t];
    }
    return solve(0, 1);
};
