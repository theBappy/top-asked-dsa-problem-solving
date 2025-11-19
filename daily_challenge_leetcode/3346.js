/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} numOperations
 * @return {number}
 */
var maxFrequency = function (nums, k, numOperations) {
    const maxEl = Math.max(...nums) + k;
    const freq = new Array(maxEl + 1).fill(0);
    for (const num of nums) {
        freq[num]++;
    }

    for (let i = 1; i <= maxEl; i++) {
        freq[i] += freq[i - 1];
    }

    let result = 0;
    for (let target = 0; target <= maxEl; target++) {
        if (freq[target] === 0) {
            continue;
        }
        const leftNum = Math.max(0, target - k);
        const rightNum = Math.min(maxEl, target + k);

        const totalCount = freq[rightNum] - (leftNum > 0 ? freq[leftNum - 1] : 0);
        const targetCount = freq[target] - (target > 0 ? freq[target - 1] : 0);
        const needConversion = totalCount - targetCount;

        const maxPossibleFreq = targetCount + Math.min(needConversion, numOperations);
        result = Math.max(result, maxPossibleFreq);
    }

    return result;
};