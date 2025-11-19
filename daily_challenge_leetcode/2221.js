
/**
 * @param {number[]} nums
 * @return {number}
 */
var triangularSum = function (nums) {
    while (nums.length > 1) {
        let temp = []
        for (let i = 0; i < nums.length - 1; i++) {
            temp.push((nums[i] + nums[i + 1]) % 10)
        }
        nums = temp
    }
    return nums[0]
};



/**
 * @param {number[]} nums
 * @return {number}
 */
var triangularSum = function (nums) {
    let n = nums.length
    for (let size = n - 1; size >= 1; size--) {
        for (let i = 0; i < size; i++) {
            nums[i] = (nums[i] + nums[i + 1]) % 10
        }
    }
    return nums[0]
};