// Two pass solution
// Tc = O(n + n) [for total sum and for leftSum-rightSum] => O(n)
// Sc = O(1)



// One pass solution
// Tc = O(n) [only for total sum]
// Sc = O(1)
/**
 * @param {number[]} nums
 * @return {number}
 */
var countPartitions = function (nums) {
    const n = nums.length
    const sum = nums.reduce((acc, val) => acc + val, 0)
    let left = 0
    let result = 0
    for (let i = 0; i < n - 1; i++) {
        const right = sum - left;
        if ((left - right) % 2 === 0) {
            result++
        }
    }
    return result
};

/**
 * @param {number[]} nums
 * @return {number}
 */
var countPartitions = function (nums) {
    const n = nums.length
    const sum = nums.reduce((acc, val) => acc + val, 0)
    if(sum % 2 === 0) return n-1
    return 0
};