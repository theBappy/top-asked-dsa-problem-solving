/**
 * @param {string[]} wordlist
 * @param {string[]} queries
 * @return {string[]}
 */
var spellchecker = function (wordlist, queries) {
    const exactWords = new Set();
    const caseMap = new Map();
    const vowelMap = new Map();

    const lower = (word) => word.toLowerCase();
    const maskVowels = (word) => word.replace(/[aeiou]/gi, '*');

    const checkForMatch = (query) => {
        if (exactWords.has(query)) {
            return query;
        }
        let lowerQuery = lower(query);
        if (caseMap.has(lowerQuery)) {
            return caseMap.get(lowerQuery);
        }
        let maskedQuery = maskVowels(lowerQuery);
        if (vowelMap.has(maskedQuery)) {
            return vowelMap.get(maskedQuery);
        }
        return "";
    };

    // Step 1: build maps
    for (const word of wordlist) {
        exactWords.add(word);

        const lowerWord = lower(word);
        if (!caseMap.has(lowerWord)) {
            caseMap.set(lowerWord, word);
        }

        const maskedWord = maskVowels(lowerWord);
        if (!vowelMap.has(maskedWord)) {
            vowelMap.set(maskedWord, word);
        }
    }

    // Step 2: process queries
    const result = [];
    for (const query of queries) {
        result.push(checkForMatch(query));
    }

    // Step 3: return results
    return result;
};
