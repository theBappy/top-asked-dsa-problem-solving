class TrieNode {
    constructor() {
        this.children = new Array(26).fill(null);
        this.isEnd = false;
    }
}

class Trie {
    constructor() {
        this.root = this.getNode();
    }

    getNode() {
        return new TrieNode();
    }

    insert(word) {
        let crawler = this.root;
        for (let char of word) {
            const idx = char.charCodeAt(0) - 'a'.charCodeAt(0);
            if (crawler.children[idx] === null) {
                crawler.children[idx] = this.getNode();
            }
            crawler = crawler.children[idx];
        }
        crawler.isEnd = true;
    }

    search(word) {
        let crawler = this.root;
        for (let i = 0; i < word.length; i++) {
            const char = word[i];
            const idx = char.charCodeAt(0) - 'a'.charCodeAt(0);
            if (crawler.children[idx] === null) {
                return word;
            }
            crawler = crawler.children[idx];
            if (crawler.isEnd) {
                return word.slice(0, i + 1);
            }
        }
        return word;
    }

    replaceWords(dictionary, sentence) {
        for (let word of dictionary) {
            this.insert(word);
        }
        const words = sentence.split(' ');
        const result = [];
        for (let word of words) {
            result.push(this.search(word));
        }
        return result.join(' ');
    }
}