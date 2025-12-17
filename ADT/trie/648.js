/**
 * @param {string[]} dictionary
 * @param {string} sentence
 * @return {string}
 */
var replaceWords = function (dictionary, sentence) {

    // Trie node constructor
    function TrieNode() {
        // 26 children for 'a' to 'z'
        // Space: O(26) → O(1)
        this.children = new Array(26).fill(null);
        this.isEndOfWord = false;
    }

    // Create root of Trie
    const root = new TrieNode();

    // Insert a word into Trie
    function insert(word) {
        let crawler = root;

        // Traverse each character of the word
        // Time: O(word.length)
        for (let i = 0; i < word.length; i++) {
            const index = word.charCodeAt(i) - 'a'.charCodeAt(0);

            // Create node if missing
            // Time: O(1)
            if (!crawler.children[index]) {
                crawler.children[index] = new TrieNode();
            }

            // Move to next node
            crawler = crawler.children[index];
        }

        // Mark end of word
        crawler.isEndOfWord = true;
    }

    // Search for shortest root prefix
    function search(word) {
        let crawler = root;

        // Traverse characters of word
        // Time: O(word.length)
        for (let i = 0; i < word.length; i++) {
            const index = word.charCodeAt(i) - 'a'.charCodeAt(0);

            // If path breaks, no root exists
            if (!crawler.children[index]) {
                return word; // O(1)
            }

            crawler = crawler.children[index];

            // If root word ends, return prefix
            if (crawler.isEndOfWord) {
                return word.substring(0, i + 1); // O(i)
            }
        }

        // No root word matched
        return word;
    }

    // Insert all dictionary words into Trie
    // Time: O(D × L)
    for (let i = 0; i < dictionary.length; i++) {
        insert(dictionary[i]);
    }

    const words = sentence.split(" "); // Time: O(S)
    const result = [];

    // Replace each word using Trie search
    // Time: O(W × M)
    for (let i = 0; i < words.length; i++) {
        result.push(search(words[i]));
    }

    // Join result into final sentence
    // Time: O(S)
    return result.join(" ");
};
