/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var hasIncreasingSubarrays = function (nums, k) {
    const n = nums.length;
    
    const isIncreasing = (s, e) => {
        for (let i = s + 1; i < e; i++) {
            if (nums[i] <= nums[i - 1]) {
                return false;
            }
        }
        return true;
    };
    
    for (let start = 0; start <= n - 2 * k; start++) {
        const first = isIncreasing(start, start + k);  
        const second = isIncreasing(start + k, start + 2 * k);  
        if (first && second) {
            return true;
        }
    }
    return false;
};


/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var hasIncreasingSubarrays = function (nums, k) {
    const n = nums.length;
    let currRun = 1
    let prevRun = 0
    for (let i = 1; i < n; i++) {
        if (nums[i] > nums[i - 1]) {
            currRun++
        } else {
            prevRun = currRun
            currRun = 1
        }

        if (currRun >= 2 * k) {
            return true
        } else if (Math.min(currRun, prevRun) >= k) {
            return true
        }
    }
    return false

};
