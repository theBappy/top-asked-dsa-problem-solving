/**
 * @param {number[]} arr
 * @return {number[]}
 */
var sortByBits = function(arr) {
    const countOneBit = (num) => {
        let count = 0
        while(num !== 0){
            count += num & 1
            num >>= 1
        }
        return count
    }
    arr.sort((a,b) => {
        const countA = countOneBit(a)
        const countB = countOneBit(b)
        return countA === countB ? a - b : countA - countB
    })
    return arr
};



var sortByBits = function(arr) {
    arr.sort((a,b) => {
        const countA = a.toString(2).split('0').join('').length
        const countB = b.toString(2).split('0').join('').length
        return countA === countB ? a - b : countA - countB
    })
    return arr
};