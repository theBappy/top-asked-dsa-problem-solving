
//  Tc = O(n + t) [for counting freq of n ,and for t*26=t loop]
//   Sc = O(n) [26 alphabets, constant space]
class Solution {
    lengthAfterTransformations(s, t) {
        const M = 10**9 + 7;
        const mp = new Array(26).fill(0);
        
        // Count frequency of each character in the string
        for (const ch of s) {
            mp[ch.charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
        }
        
        // Perform transformations t times
        for (let _ = 0; _ < t; _++) {
            const temp = new Array(26).fill(0);
            for (let i = 0; i < 26; i++) {
                const freq = mp[i];
                if (i < 25) {  // 'a' to 'y'
                    temp[i + 1] = (temp[i + 1] + freq) % M;
                } else {  // 'z'
                    temp[0] = (temp[0] + freq) % M;
                    temp[1] = (temp[1] + freq) % M;
                }
            }
            mp.splice(0, 26, ...temp);
        }
        
        // Calculate the total length after transformations
        const result = mp.reduce((a, b) => (a + b) % M, 0);
        return result;
    }
}