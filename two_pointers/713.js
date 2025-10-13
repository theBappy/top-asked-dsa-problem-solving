/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numSubarrayProductLessThanK = function (nums, k) {
    const n = nums.length;
    let result = 0;
    let product = 1;
    let i = 0, j = 0;
    while (j < n) {
        product *= nums[j];
        while (i <= j && product >= k) {
            product = (product / nums[i]) >> 0;  
            i += 1;
        }
        result += (j - i + 1); 
        j += 1;
    }
    return result;
};