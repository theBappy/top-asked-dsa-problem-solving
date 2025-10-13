/**
 * @param {number[]} nums
 * @return {number}
 */
var countCompleteSubarrays = function (nums) {
    const n = nums.length;
    const uniqueElements = new Set(nums);
    const c = uniqueElements.size;
    let i = 0;
    let j = 0;
    let result = 0;
    const mp = new Map();

    while (j < n) {
        mp.set(nums[j], (mp.get(nums[j]) || 0) + 1)
        while(mp.size === c){
            result += (n - j)
            mp.set(nums[i], mp.get(nums[i]) - 1)
            if(mp.get(nums[i]) === 0){
                mp.delete(nums[i])
            }
            i += 1
        }
        j += 1
    }
    return result
};