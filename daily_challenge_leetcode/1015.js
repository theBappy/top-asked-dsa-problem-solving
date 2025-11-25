/**
 * @param {number} k
 * @return {number}
 */
var smallestRepunitDivByK = function (k) {
    if (k === 1) {
        return 1
    }
    let num = 0
    for (let length = 1; length <= k; length++) {
        num = (num * 10 + 1) % k
        if (num === 0) {
            return length
        }
    }
    return -1
};