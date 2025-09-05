/**
 * @param {number} columnNumber
 * @return {string}
 */
var convertToTitle = function(cn) {
    let result = []
    while(cn > 0){
        cn -= 1;
        let remainder = cn % 26
        let ch = String.fromCharCode('A'.charCodeAt(0) + remainder)
        result.push(ch)
        cn = Math.floor(cn / 26)
    }
    result.reverse()
    return result.join('')
};