class TrieNode {
    constructor() {
        this.children = new Array(26).fill(null);
        this.isEndOfWord = false;
    }
}

class Trie {

    constructor() {
        this.root = new TrieNode();
    }

    insert(word) {
        let crawler = this.root;

        for (let ch of word) {
            let index = ch.charCodeAt(0) - 'a'.charCodeAt(0);
            if (crawler.children[index] === null) {
                crawler.children[index] = new TrieNode();
            }
            crawler = crawler.children[index];
        }

        crawler.isEndOfWord = true;
    }

    search(word) {
        let crawler = this.root;

        for (let ch of word) {
            let index = ch.charCodeAt(0) - 'a'.charCodeAt(0);
            if (crawler.children[index] === null) {
                return false;
            }
            crawler = crawler.children[index];
        }

        return crawler !== null && crawler.isEndOfWord;
    }

    startsWith(prefix) {
        let crawler = this.root;

        for (let ch of prefix) {
            let index = ch.charCodeAt(0) - 'a'.charCodeAt(0);
            if (crawler.children[index] === null) {
                return false;
            }
            crawler = crawler.children[index];
        }

        return true;
    }
}
