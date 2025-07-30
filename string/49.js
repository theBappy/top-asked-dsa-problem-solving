var getSignature = function(s) {
    const count = Array(26).fill(0);
    for (const c of s) {
        count[c.charCodeAt(0) - 'a'.charCodeAt(0)]++;
    }

    const result = [];
    for (let i = 0; i < 26; i++) {
        if (count[i] !== 0) {
            result.push(String.fromCharCode(i + 'a'.charCodeAt(0)), count[i].toString());
        }
    }

    return result.join('');
};

var groupAnagrams = function(strs) {
    const result = [];
    const groups = new Map();
    for(const s of strs){
        const signature = getSignature(s)
        if(!groups.has(signature)){
            groups.set(signature, [])
        }
        groups.set(signature).push(s)
    }
    groups.forEach(value => result.push(value))
    return result
}


//  Tc = O(n * klogk) [k = maximum size of string in the input and n = size of input]
//  Sc = O(n.k)
class Solution {
    groupAnagrams(strs){
        const n = strs.length
        const result = []
        const mp = new Map()
        for(let i = 0; i<n; i++){
            const temp = strs[i].split('').sort().join('')
            if(!mp.has(temp)){
                mp.set(temp,[])
            }
            mp.get(temp).push(strs[i])
        }
        for(const i of mp.values()){
            result.push(it)
        }
        return result
    }
}

