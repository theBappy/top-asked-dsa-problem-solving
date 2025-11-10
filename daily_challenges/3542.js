/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function (nums) {
    const st = []
    let ops = 0
    for (let i = 0; i < nums.length; i++) {
        while (st.length > 0 && st[st.length - 1] > nums[i]) {
            st.pop()
        }
        if (nums[i] === 0) {
            continue
        }
        if (st.length === 0 || st[st.length - 1] < nums[i]) {
            st.push(nums[i])
            ops++
        }
    }
    return ops
};