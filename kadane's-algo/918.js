var maxSubarraySumCircular = function (nums) {
    let total = 0;
    let currMax = 0, maxSum = nums[0];
    let currMin = 0, minSum = nums[0];

    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        currMax = Math.max(currMax + num, num);  
        maxSum = Math.max(maxSum, currMax);

        currMin = Math.min(currMin + num, num);  
        minSum = Math.min(minSum, currMin);

        total += num;
    }

    
    return maxSum > 0 ? Math.max(maxSum, total - minSum) : maxSum;
};
