var numSquares = function(n) {
    // Memoization array to store computed results
    const memo = new Array(n + 1).fill(-1);
    
    function helper(num) {
        // Base case: 0 requires 0 perfect squares
        if (num === 0) return 0;
        
        // Return memoized result if already computed
        if (memo[num] !== -1) return memo[num];
        
        let minCount = Infinity;
        
        // Try all perfect squares less than or equal to num
        for (let i = 1; i * i <= num; i++) {
            const result = 1 + helper(num - i * i);
            minCount = Math.min(minCount, result);
        }
        
        // Store result in memo array and return
        memo[num] = minCount;
        return minCount;
    }
    
    return helper(n);
};



// another approach
var numSquares = function(n) {
    const dp = new Array(n + 1).fill(Infinity);
    dp[0] = 0;
    
    for (let i = 1; i <= n; i++) {
        for (let j = 1; j * j <= i; j++) {
            dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
        }
    }
    
    return dp[n];
};
