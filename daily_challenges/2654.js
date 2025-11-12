/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function (nums) {
    const n = nums.length
    let count1 = 0
    for (let i = 0; i < n; i++) {
        if (nums[i] === 1) count1++
    }
    if (count1 > 0) return n - count1
    const gcd = (a, b) => {
        while (b !== 0) {
            [a, b] = [b, a % b]
        }
        return a
    }
    let minOps = Number.MAX_SAFE_INTEGER
    for (let i = 0; i < n - 1; i++) {
        let currentGCD = nums[i]
        for (let j = i + 1; j < n; j++) {
            currentGCD = gcd(currentGCD, nums[j])
            if (currentGCD === 1) {
                minOps = Math.min(minOps, j - i)
                break
            }
        }
    }
    if (minOps === Number.MAX_SAFE_INTEGER) {
        return -1
    }
    return minOps + (n - 1)
};