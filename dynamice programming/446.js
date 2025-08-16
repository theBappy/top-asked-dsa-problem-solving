function numberOfArithmeticSlices(nums) {
    const n = nums.length;
    let result = 0;
    const dp = new Array(n).fill().map(() => new Map());
    
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < i; j++) {
            const diff = nums[i] - nums[j];
            const count_at_j = dp[j].get(diff) || 0;
            
            dp[i].set(diff, (dp[i].get(diff) || 0) + count_at_j + 1);
            result += count_at_j;
        }
    }
    return result;
}
