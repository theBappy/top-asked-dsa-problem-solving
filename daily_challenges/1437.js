/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var kLengthApart = function (nums, k) {
    const n = nums.length
    let lastOne = - (k + 1)
    for (let i = 0; i < n; i++) {
        if (nums[i] === 1) {
            if (i - lastOne - 1 < k) {
                return false
            }
            lastOne = i
        }
    }
    return true
};