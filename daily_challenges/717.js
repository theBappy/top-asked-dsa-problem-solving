/**
 * @param {number[]} bits
 * @return {boolean}
 */
var isOneBitCharacter = function(bits) {
    const n = bits.length
    let i = 0
    while(i < n - 1){
        i += (bits[i] === 1) ? 2 : 1
    }
    return i === n - 1
};


/**
 * @param {number[]} bits
 * @return {boolean}
 */
var isOneBitCharacter = function (bits) {
    let n = bits.length
    let count1 = 0
    for (let i = n - 2; i >= 0 && bits[i] === 1; i--) {
        count1++
    }
    return count1 % 2 === 0
};