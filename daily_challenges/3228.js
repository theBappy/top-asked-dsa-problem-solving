/**
 * @param {string} s
 * @return {number}
 */
var maxOperations = function (s) {
    const n = s.length
    let result = 0
    let i = 0
    let count1 = 0
    while (i < n) {
        if (s[i] === '0') {
            result += count1
            while (i < n && s[i] === '0') {
                i++
            }
        } else {
            count1++
            i++
        }
    }
    return result
};