/**
 * @param {number[]} nums
 * @return {number}
 */
var repeatedNTimes = function (nums) {
    const st = new Set()
    for (const num of nums) {
        if (st.has(num))
            return num
        st.add(num)
    }
    return -1
};


/**
 * @param {number[]} nums
 * @return {number}
 */
var repeatedNTimes = function (nums) {
    const freq = new Array(10001).fill(0)
    for (const num of nums) {
        freq[num]++
        if (freq[num] > 1)
            return num
    }
    return -1
};


/**
 * @param {number[]} nums
 * @return {number}
 */
var repeatedNTimes = function (nums) {
    const n = nums.length
    for (let i = 2; i < n; i++) {
        if (nums[i] === nums[i - 1] || nums[i] === nums[i - 2]) {
            return nums[i]
        }
    }
    return nums[n-1]
};