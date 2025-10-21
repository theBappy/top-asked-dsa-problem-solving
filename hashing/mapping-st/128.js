/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
    const numsSet = new Set(nums);
    let maxLen = 0;
    for (const num of numsSet) {
        if (!numsSet.has(num - 1)) {
            let currNum = num;
            let currLen = 1;
            while (numsSet.has(currNum + 1)) {
                currLen += 1;
                currNum += 1;
            }
            maxLen = Math.max(maxLen, currLen);
        }
    }
    return maxLen;
};