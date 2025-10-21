/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
    const n = nums.length
    const mp = new Map()
    for (const num of nums) {
        mp.set(num, (mp.get(num) || 0) + 1)
    }
    const bucket = Array.from({ length: n + 1 }, () => [])
    for (const [element, freq] of mp.entries()) {
        bucket[freq].push(element)
    }
    const result = []
    for (let i = n; i > 0; i--) {
        if (bucket[i].length === 0) continue
        while (bucket[i].length > 0 && k > 0) {
            result.push(bucket[i].pop())
            k--
        }
    }
    return result
};