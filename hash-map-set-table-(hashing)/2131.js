//  Tc = O(n) [number of words]
//  Sc = O(n)
class Solution {
    longestPalindrome(words) {
        const mp = new Map();
        let result = 0;
        
        for (const word of words) {
            const reversedWord = word.split('').reverse().join('');
            if (mp.get(reversedWord) > 0) {
                result += 4;
                mp.set(reversedWord, mp.get(reversedWord) - 1);
            } else {
                mp.set(word, (mp.get(word) || 0) + 1);
            }
        }
        
        // check equal character words and use only once
        for (const [word, count] of mp.entries()) {
            if (word[0] === word[1] && count > 0) {
                result += 2;
                break;
            }
        }
        return result;
    }
}