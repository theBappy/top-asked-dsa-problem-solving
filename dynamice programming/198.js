var rob = function(nums) {
    const n = nums.length;
    const t = new Array(n).fill(-1); // Initialize memoization array once
    
    const solve = (i) => {
        if (i >= n) return 0;
        if (t[i] !== -1) return t[i];
        
        const steal = nums[i] + solve(i + 2);
        const skip = solve(i + 1);
        
        return t[i] = Math.max(steal, skip);
    };
    
    return solve(0);
};