/**
 * @param {number[]} nums
 * @param {number} value
 * @return {number}
 */
function findSmallestInteger(nums, value) {
    const mp = new Map();
    for (const num of nums) {
        const r = ((num % value) + value) % value;
        mp.set(r, (mp.get(r) || 0) + 1);
    }
    let MEX = 0;
    while ((mp.get(MEX % value) || 0) > 0) {
        mp.set(MEX % value, mp.get(MEX % value) - 1);
        MEX += 1;
    }
    return MEX;
}