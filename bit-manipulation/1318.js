/**
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number}
 */
var minFlips = function (a, b, c) {
    let result = 0;

    while (a > 0 || b > 0 || c > 0) {
        if ((c & 1) === 1) {
            if ((a & 1) === 0 && (b & 1) === 0) {
                result += 1;
            }
        } else {
            result += (a & 1) + (b & 1);
        }

        a >>= 1;
        b >>= 1;
        c >>= 1;
    }

    return result;
};



var minFlips = function(a, b, c) {
    const countOnes = (num) => {
        return num.toString(2).split('0').join('').length;
    }
    
    // Calculate the number of bits that need to be flipped
    const temp = (a | b) ^ c
    return countOnes(temp) + countOnes(temp & (a & b));
};
