/**
 * @param {string[]} words
 * @param {string} target
 * @return {number}
 */
const numWays = function(words, target) {
    const m = target.length;
    const k = words[0].length;
    const MOD = 1e9 + 7;
    
    // Initialize frequency array (26 letters x k columns)
    const freq = Array.from({ length: 26 }, () => new Array(k).fill(0));
    
    // Populate frequency array
    for (let col = 0; col < k; col++) {
        for (const word of words) {
            const char = word.charCodeAt(col) - 97; // 'a' = 97
            freq[char][col]++;
        }
    }
    
    // Initialize memoization table (m rows x k columns)
    const memo = Array.from({ length: m }, () => new Array(k).fill(-1));
    
    // Recursive DP function with memoization
    function dp(i, j) {
        if (i === m) return 1;  // Target fully formed
        if (j === k) return 0;  // No more columns to choose from
        
        if (memo[i][j] !== -1) return memo[i][j];
        
        // Option 1: Skip current column
        const skip = dp(i, j + 1) % MOD;
        
        // Option 2: Take current character
        const charCode = target.charCodeAt(i) - 97;
        const take = (freq[charCode][j] * dp(i + 1, j + 1)) % MOD;
        
        return memo[i][j] = (skip + take) % MOD;
    }
    
    return dp(0, 0);
};
