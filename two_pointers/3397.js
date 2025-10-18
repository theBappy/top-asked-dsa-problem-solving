/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxDistinctElements = function (nums, k) {
    const n = nums.length
    nums.sort((a, b) => a - b)
    let count = 0
    let prev = -Infinity
    for (let i = 0; i < n; i++) {
        const minVal = nums[i] - k
        if (prev < minVal) {
            prev = minVal
            count += 1
        }
        else if (prev < nums[i] + k) {
            prev += 1
            count += 1
        }
    }
    return count
};