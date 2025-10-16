
//this will give TLE in js
/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function (s1, s2) {
    const n = s1.length
    const m = s2.length
    if (n > m) return false
    const sortedS1 = s1.split('').sort().join('')
    for (let i = 0; i <= m - n; i++) {
        const sortedS2 = s2.slice(i, i + n).split('').sort().join('')
        if (sortedS1 === sortedS2) {
            return true;
        }
    }
    return false
};