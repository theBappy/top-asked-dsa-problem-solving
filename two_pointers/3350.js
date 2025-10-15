/**
 * @param {number[]} nums
 * @return {number}
 */
var maxIncreasingSubarrays = function (nums) {
    const n = nums.length
    let currRun = 1, prevRun = 0, K = 0
    for (let i = 1; i < n; i++) {
        if (nums[i] > nums[i - 1]) {
            currRun++
        }
        else {
            prevRun = currRun
            currRun = 1
        }
        K = Math.max(K, Math.floor(currRun / 2))
        K = Math.max(K, Math.min(prevRun, currRun))
    }
    return K
};