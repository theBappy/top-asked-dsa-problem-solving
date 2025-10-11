

/**
 * @param {number[]} power
 * @return {number}
 */
var maximumTotalDamage = function (power) {
    const mp = new Map()
    for (let p of power) {
        mp.set(p, (mp.get(p) || 0) + 1)
    }
    const nums = Array.from(mp.keys()).sort((a, b) => a - b)
    const n = nums.length
    const t = new Array(n).fill(-1)

    function solve(i) {
        if (i >= n) return 0
        if (t[i] !== -1) return t[i]
        const skip = solve(i + 1)
        const target = nums[i] + 3
        const j = lowerBound(nums, target, i + 1)
        const take = nums[i] * mp.get(nums[i]) + solve(j)
        t[i] = Math.max(take, skip)
        return t[i]
    }
    function lowerBound(arr, target, start) {
        let low = start
        let high = arr.length
        while (low < high) {
            let mid = Math.floor((low + high) / 2)
            if (arr[mid] < target) {
                low = mid + 1
            } else {
                high = mid
            }
        }
        return low
    }
    return solve(0)
};