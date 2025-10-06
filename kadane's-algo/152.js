/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function (nums) {
    const n = nums.length
    let r = nums[0]
    let imax = r
    let imin = r
    for (let i = 1; i < n; i++) {
        if (nums[i] < 0){
            [imax, imin] = [imin, imax]
        }
        imax = Math.max(nums[i], imax * nums[i])
        imin = Math.min(nums[i], imin * nums[i])
        r = Math.max(r, imax)
    }
    return r
};