/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
    let result = 0
    for (let bit = 0; bit <= 31; bit++) {
        let temp = 1 << bit
        let countZeros = 0
        let countOnes = 0
        for (let num of nums) {
            if ((num & temp) == 0) {
                countZeros++
            } else {
                countOnes++
            }
        }
        if (countOnes % 3 == 1) {
            result = result | temp
        }
    }
    if(result >= 2**31){
        result -= 2 **31
    }
    return result
};