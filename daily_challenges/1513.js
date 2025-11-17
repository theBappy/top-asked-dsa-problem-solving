/**
 * @param {string} s
 * @return {number}
 */
var numSub = function (s) {
    const M = 1e9 + 7
    let result = 0
    let count1 = 0
    for (const ch of s) {
        if (ch === '1') {
            count1++
        }
        else {
            result = (result + (count1 * (count1 + 1) / 2)) % M
            count1 = 0
        }
    }
    result = (result + (count1 * (count1 + 1) / 2)) % M
    return result
};


/**
 * @param {string} s
 * @return {number}
 */
var numSub = function (s) {
    const M = 1e9 + 7
    let result = 0
    let count1 = 0
    for (const ch of s) {
        if (ch === '1') {
            count1++
            result = (result + count1) % M
        } else {
            count1 = 0
        }
    }
    return result
};