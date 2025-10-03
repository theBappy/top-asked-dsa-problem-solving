/**
 * @param {number[]} nums
 * @return {number[]}
 */
var applyOperations = function(nums) {
   const n = nums.length
    for(let i = 0; i < n-1; i++){
        if(nums[i] == nums[i + 1]){
            nums[i] *= 2
            nums[i + 1] = 0
        }
    }
    let j = 0
    for(let i = 0; i < n; i++){
        if(nums[i] !== 0){
            nums[j] = nums[i]
            j += 1
        }
    }
    while(j < n){
        nums[j] = 0
        j += 1
    }
    return nums
};



/**
 * @param {number[]} nums
 * @return {number[]}
 */
var applyOperations = function (nums) {
    const n = nums.length
    let j = 0
    for (let i = 0; i < n; i++) {
        if (i + 1 < n && nums[i] == nums[i + 1] && nums[i] !== 0) {
            nums[i] *= 2
            nums[i + 1] = 0
        }
        if (nums[i] !== 0) {
            if (i !== j) {
                [nums[j], nums[i]] = [nums[i], nums[j]]
            }
            j += 1
        }

    }
    return nums
};