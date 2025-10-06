/**
 * @param {number[]} nums
 * @return {number}
 */
var maxAbsoluteSum = function (nums) {
    const n = nums.length

    let maxSum = nums[0];
    let minSum = nums[0];

    let currSumMax = nums[0];
    let currSumMin = nums[0];

    for (let i = 1; i < n; i++) {
        currSumMax = Math.max(nums[i], currSumMax + nums[i])
        maxSum = Math.max(maxSum, currSumMax)

        currSumMin = Math.min(nums[i], currSumMin + nums[i])
        minSum = Math.min(minSum, currSumMin)
    }
    return Math.max(maxSum, Math.abs(minSum))
};