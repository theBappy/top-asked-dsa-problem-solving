/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function (nums, k) {
    const n = nums.length
    const deq = []
    const result = []
    for (let i = 0; i < n; i++) {
        while (deq.length && deq[0] <= i - k) {
            deq.shift()
        }
        while (deq.length && nums[i] > nums[deq[deq.length - 1]]) {
            deq.pop()
        }
        deq.push(i)
        if (i >= k - 1) {
            result.push(nums[deq[0]])
        }
    }
    return result
};