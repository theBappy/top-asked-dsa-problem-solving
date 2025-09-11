/**
 * @param {string} s
 * @return {string}
 */
var sortVowels = function(s) {
    const vowels = Array.from(s).filter(ch => "AEIOUaeiou".includes(ch))
    vowels.sort()
    let idx = 0
    const res = Array.from(s)
    for(let i = 0; i <res.length; i++){
        if("AEIOUaeiou".includes(res[i])){
            res[i] = vowels[idx]
            idx++
        }
    }
    return res.join("")
};