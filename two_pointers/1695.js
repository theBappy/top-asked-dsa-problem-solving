

/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumUniqueSubarray = function (nums) {
    let res = 0;
    let cur_sum = 0;
    let start = 0;
    const seen = new Set();
    for (let end = 0; end < nums.length; end++) {
        while (seen.has(nums[end])) {
            seen.delete(nums[start]);
            cur_sum -= nums[start];
            start += 1;
        }
        cur_sum += nums[end];
        seen.add(nums[end]);
        res = Math.max(res, cur_sum);
    }
    return res;
};