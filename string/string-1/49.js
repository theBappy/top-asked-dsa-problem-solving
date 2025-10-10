/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const mp = new Map()
    for(const s of strs){
        const temp = s.split('').sort().join('')
        if(!mp.has(temp)){
            mp.set(temp, [])
        }
        mp.get(temp).push(s)
    }
    return Array.from(mp.values())
};


var groupAnagrams = function(strs) {
    const mp = new Map()
    
    const generate = (s) => {
        const count = new Array(26).fill(0)
        for(const ch of s){
            count[ch.charCodeAt(0) - 'a'.charCodeAt(0)] += 1
        }
        const new_s = []
        for(let i = 0; i < 26; i++){
            if(count[i] > 0){
                new_s.push(String.fromCharCode(i + 'a'.charCodeAt(0)).repeat(count[i]))
            }
        }
        return new_s.join('')
    }

    for(const s of strs){
        const new_s = generate(s)
        if(!mp.has(new_s)){
            mp.set(new_s, [])
        }
        mp.get(new_s).push(s)
    }
    return Array.from(mp.values())
};