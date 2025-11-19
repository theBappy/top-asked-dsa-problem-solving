/**
 * @param {string} s
 * @return {boolean}
 */
var hasSameDigits = function(s) {
    let n = s.length
    while(n > 2){
        let newStr = ""
        for(let i = 0; i < n-1; i++){
            newStr +=  ((parseInt(s[i]) + parseInt(s[i+1])) % 10).toString()
        }
        s = newStr;
        n -= 1
    }
    return s[0] === s[1]
};