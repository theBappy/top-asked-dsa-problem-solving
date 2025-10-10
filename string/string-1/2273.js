/**
 * @param {string[]} words
 * @return {string[]}
 */
var removeAnagrams = function(words) {
    const areAnagrams = (s1, s2) => {
        const count = new Array(26).fill(0); // reset for each call
        for (const x of s1) {
            count[x.charCodeAt(0) - 97]++;
        }
        for (const x of s2) {
            count[x.charCodeAt(0) - 97]--;
        }
        return count.every(val => val === 0);
    };

    let i = 1;
    while (i < words.length) {
        if (areAnagrams(words[i - 1], words[i])) {
            words.splice(i, 1);
        } else {
            i++;
        }
    }
    return words;
};


// Tc = O(n.m)
// Sc = O(n)
var removeAnagrams = function(words) {
    const res = [words[0]];
    const areAnagrams = (s1, s2) => {
        const count = new Array(26).fill(0);
        for (const x of s1) count[x.charCodeAt(0) - 97]++;
        for (const x of s2) count[x.charCodeAt(0) - 97]--;
        return count.every(v => v === 0);
    };
    for (let i = 1; i < words.length; i++) {
        if (!areAnagrams(words[i - 1], words[i])) res.push(words[i]);
    }
    return res;
};
