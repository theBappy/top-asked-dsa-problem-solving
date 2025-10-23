/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} numOperations
 * @return {number}
 */
var maxFrequency = function (nums, k, numOperations) {
    const maxVal = Math.max(...nums) + k;
    const diff = new Map();
    const freq = new Map();

    for (const num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1);

        const l = Math.max(num - k, 0);
        const r = Math.min(num + k, maxVal);

        diff.set(l, (diff.get(l) || 0) + 1);
        diff.set(r + 1, (diff.get(r + 1) || 0) - 1);

        if (!diff.has(num)) {
            diff.set(num, 0);
        }
    }

    let result = 1;
    let cumSum = 0;

    const sortedKeys = Array.from(diff.keys()).sort((a, b) => a - b);

    for (const target of sortedKeys) {
        diff.set(target, diff.get(target) + cumSum);

        const targetFreq = freq.get(target) || 0;
        const needConversion = diff.get(target) - targetFreq;

        const maxPossibleFreq = Math.min(needConversion, numOperations);

        result = Math.max(result, targetFreq + maxPossibleFreq);

        cumSum = diff.get(target);
    }

    return result;
};