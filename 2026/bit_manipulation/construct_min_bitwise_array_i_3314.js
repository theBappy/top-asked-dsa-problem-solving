/**
 * @param {number[]} nums
 * @return {number[]}
 */
var minBitwiseArray = function(nums) {
    const result = []
    for(const num of nums){
        let found = false
        for(let x = 0; x < num; x++){
            if((x | (x + 1)) === num){
                result.push(x)
                found = true
                break
            }
        }
        if(!found){
            result.push(-1)
        }
    }
    return result
};


/**
 * @param {number[]} nums
 * @return {number[]}
 */
var minBitwiseArray = function (nums) {
    const result = []
    for (const num of nums) {
        if (num === 2) {
            result.push(-1)
            continue
        }
        let found = false
        for (let j = 1; j < 32; j++) {
            if ((num & (1 << j)) > 0) {
                continue
            }
            result.push(num ^ (1 << (j - 1)))
            found = true
            break
        }
        if (!found) {
            result.push(-1)
        }
    }
    return result
};