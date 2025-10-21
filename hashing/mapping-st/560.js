/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function (nums, k) {
    let subNum = { 0 : 1 }
    let total = 0, count = 0
    for (const num of nums) {
        total += num
        if (subNum[total - k] !== undefined) {
            count += subNum[total - k]
        }
        subNum[total] = (subNum[total] || 0) + 1
    }
    return count
};