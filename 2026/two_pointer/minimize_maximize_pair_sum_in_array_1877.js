/**
 * @param {number[]} nums
 * @return {number}
 */
var minPairSum = function (nums) {
    nums.sort((a, b) => a - b)
    let maxR = 0
    let i = 0, j = nums.length - 1
    while (i < j) {
        let sum = nums[i] + nums[j]
        maxR = Math.max(maxR, sum)
        i++
        j--
    }
    return maxR
};