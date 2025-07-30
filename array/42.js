function trap(height) {
    // Handle edge case: empty array
    if (!height || height.length === 0) return 0;
    
    const n = height.length;
    let totalWater = 0;
    
    // Arrays to track max heights to the left/right of each position
    const leftMax = new Array(n).fill(0);
    const rightMax = new Array(n).fill(0);
    
    // Left pass: Track max height to the left of each index
    leftMax[0] = height[0];
    for (let i = 1; i < n; i++) {
        leftMax[i] = Math.max(leftMax[i - 1], height[i]);
    }
    
    // Right pass: Track max height to the right of each index
    rightMax[n - 1] = height[n - 1];
    for (let i = n - 2; i >= 0; i--) {
        rightMax[i] = Math.max(rightMax[i + 1], height[i]);
    }
    
    // Calculate trapped water at each position
    for (let i = 0; i < n; i++) {
        const waterLevel = Math.min(leftMax[i], rightMax[i]);
        totalWater += waterLevel - height[i];
    }
    
    return totalWater;
}