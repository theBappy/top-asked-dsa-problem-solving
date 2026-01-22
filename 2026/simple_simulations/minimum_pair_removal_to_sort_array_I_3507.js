/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumPairRemoval = function(nums) {
    let operations = 0
    const minPairSum = () => {    
    let minSum = Number.MAX_SAFE_INTEGER
    let index = 1
    for(let i = 0; i < nums.length - 1; i++){
        if(nums[i] + nums[i+1] < minSum){
            index = i
            minSum = nums[i] + nums[i+1]
        }
    }
    return index
    }
    const isSorted = (arr) => {
        for(let i = 1; i< arr.length; i++){
            if(arr[i] < arr[i-1]) return false
        }
        return true
    }
    while(!isSorted(nums)){
        let index = minPairSum(nums)
        nums[index] = nums[index] + nums[index+1]
        nums.splice(index + 1, 1)
        operations++
    }
    return operations
};