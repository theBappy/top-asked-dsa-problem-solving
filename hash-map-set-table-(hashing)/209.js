class Solution {
    wordPattern(pattern, s) {
        const charToIndex = {};
        const wordToIndex = {};
        const tokens = s.split(" ");
        if (pattern.length !== tokens.length) {
            return false;
        }
        for (let i = 0; i < pattern.length; i++) {
            const char = pattern[i];
            const token = tokens[i];
            if (!(char in charToIndex)) {
                charToIndex[char] = i;
            }
            if (!(token in wordToIndex)) {
                wordToIndex[token] = i;
            }
            if (charToIndex[char] !== wordToIndex[token]) {
                return false;
            }
        }
        return true;
    }
}