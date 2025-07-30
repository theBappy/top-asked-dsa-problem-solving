
// Time Complexity:
// - Basic: O(n + m*26) → O(n + m) (26 letters = constant)
// - Optimized: Same complexity but faster in practice

// Space Complexity: O(1)
// - Fixed-size frequency arrays (26 elements)

function checkInclusion(s1, s2){
    const n = s1.length
    const m = s2.length
    if(n > m) return false
    const s1Freq = new Array(26).fill(0)
    const s2Freq = new Array(26).fill(0)

    for(const ch of s1) {
        s1Freq[ch.charCodeAt(0) - 'a'.charCodeAt(0)] += 1
    }
    let i = 0
    let j = 0
    while(j < m){
        s2Freq[s2.charCodeAt(j) - 'a'.charCodeAt(0)] += 1
        if(j - i + 1 > n){
            s2Freq[s2.charCodeAt(i) - 'a'.charCodeAt(0)] -= 1
            i += 1
        }
        if(s1.toString() === s2.toString) return true
        j += 1
    }
    return false
}



function checkInclusion(s1, s2) {
    const n = s1.length;
    const m = s2.length;
    if (n > m) {
        return false;
    }
    

    const s1Freq = new Array(26).fill(0);
    const s2Freq = new Array(26).fill(0);
    
    for (const ch of s1) {
        s1Freq[ch.charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
    }
    
    let i = 0;
    let j = 0;
    while (j < m) {
        s2Freq[s2.charCodeAt(j) - 'a'.charCodeAt(0)] += 1;
        if (j - i + 1 > n) {
            s2Freq[s2.charCodeAt(i) - 'a'.charCodeAt(0)] -= 1;
            i += 1;
        }
        if (s1Freq.toString() === s2Freq.toString()) {
            return true;
        }
        j += 1;
    }
    
    return false;
}