/**
 * @param {number[]} nums
 * @return {boolean}
 */
var find132pattern = function (nums) {
    const n = nums.length
    let num3 = -Infinity
    const st = []
    for (let i = n - 1; i >= 0; i--) {
        if (nums[i] < num3) {
            return true
        }
        while (st.length > 0 && st[st.length - 1] < nums[i]) {
            num3 = st.pop()
        }
        st.push(nums[i])
    }
    return false
};