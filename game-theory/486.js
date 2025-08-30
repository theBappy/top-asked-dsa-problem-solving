var predictTheWinner = function(nums) {
    const n = nums.length;
    // Initialize memo table based on n
    const t = Array.from({length: n}, () => Array(n).fill(-1));
    
    const solve = (i, j) => {
        if (i > j) return 0;
        if (i === j) return nums[i];
        if (t[i][j] !== -1) return t[i][j];
        
        // If player picks nums[i], opponent can choose from (i+1, j)
        // Opponent will minimize player's next gain, so we take min of next states
        let take_i = nums[i] + Math.min(solve(i+2, j), solve(i+1, j-1));
        
        // If player picks nums[j], opponent can choose from (i, j-1)
        let take_j = nums[j] + Math.min(solve(i+1, j-1), solve(i, j-2));
        
        t[i][j] = Math.max(take_i, take_j);
        return t[i][j];
    }
    
    const total_score = nums.reduce((a,b) => a+b, 0);
    const p1 = solve(0, n - 1);
    const p2 = total_score - p1;
    return p1 >= p2;
};