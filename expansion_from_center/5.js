/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
    const n = s.length
    if(n <= 1){
        return s
    }
    let start = 0
    let maxlen = 1
    const expandAroundCenter = (left, right) => {
        while(left >= 0 && right < n && s[left] == s[right]){
            left--
            right++
        }
        return right - left - 1
    }
    for(let i = 0; i < n; i++){
        const len1 = expandAroundCenter(i, i)
        const len2 = expandAroundCenter(i, i+1)
        const currlen = Math.max(len1, len2)
        if(currlen > maxlen){
            maxlen = currlen
            start = i - Math.floor((currlen - 1)/2)
        }
    }
    return s.substring(start, start + maxlen)
};