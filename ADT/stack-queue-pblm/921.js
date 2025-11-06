/**
 * @param {string} s
 * @return {number}
 */
var minAddToMakeValid = function (s) {
    let size = 0
    let open = 0
    for (const ch of s) {
        if (ch === '(') {
            size++
        } else if (size > 0) {
            size--
        } else {
            open++
        }
    }
    return size + open
};