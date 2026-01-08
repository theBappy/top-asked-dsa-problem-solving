/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var maxDotProduct = function (nums1, nums2) {
    let m = nums1.length;
    let n = nums2.length;
    const t = Array.from({ length: 501 }, () => Array(501).fill(-1e9));
    const solve = (i, j) => {
        if (i === m || j === n) {
            return -1e9;
        }
        if (t[i][j] !== -1e9) {
            return t[i][j];
        }
        const val = nums1[i] * nums2[j];
        const take_i_j = solve(i + 1, j + 1) + val;
        const take_i = solve(i, j + 1);
        const take_j = solve(i + 1, j);
        return t[i][j] = Math.max(val, take_i_j, take_i, take_j);
    };
    return solve(0, 0);
};