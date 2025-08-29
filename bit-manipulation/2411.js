/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallestSubarrays = function(nums) {
    const n = nums.length
    const result = new Array(n).fill(0)
    const setBitIndex = new Array(32).fill(-1)

    for (let i = n-1; i >=0 ; i--){
        let endIndex = i
        for(let j = 0; j < 32; j++){
            if(!(nums[i] & (1 << j))){
                if(setBitIndex[j] !== -1){
                    endIndex = Math.max(endIndex, setBitIndex[j])
                }
            }else{
                setBitIndex[j] = i
            }
        }
        result[i] = endIndex - i + 1
    }
    return result
};