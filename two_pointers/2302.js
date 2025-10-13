/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countSubarrays = function (nums, k) {
    const n = nums.length
    let result = 0
    let i = 0
    let j = 0
    let sum = 0
    while (j < n) {
        sum += nums[j]
        while (i <= j && sum * (j - i + 1) >= k) {
            sum -= nums[i]
            i++
        }
        result += (j - i + 1)
        j++
    }
    return result
};