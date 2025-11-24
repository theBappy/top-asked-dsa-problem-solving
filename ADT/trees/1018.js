/**
 * @param {number[]} nums
 * @return {boolean[]}
 */
var prefixesDivBy5 = function(nums) {
    const n = nums.length
    const result = new Array(n)
    let remain = 0
    for(let i = 0; i < n; i++){
        remain = (remain * 2 + nums[i]) % 5
        result[i] = (remain === 0)
    }
    return result
};