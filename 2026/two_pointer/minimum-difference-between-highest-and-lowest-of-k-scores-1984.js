/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minimumDifference = function (nums, k) {
    nums.sort((a, b) => a - b);

    let minDiff = Number.MAX_SAFE_INTEGER;

    for (let i = k - 1; i < nums.length; i++) {
        let minEl = nums[i - k + 1];
        let maxEl = nums[i];
        minDiff = Math.min(minDiff, maxEl - minEl);
    }

    return minDiff;
};