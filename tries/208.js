
class TrieNode {
  constructor() {
    // Array to store children nodes, one for each letter of the alphabet.
    this.children = new Array(26).fill(null); 
    // Boolean flag to mark if a word ends at this node.
    this.isEndOfWord = false; 
  }
}

class Trie {
  constructor() {
    this.root = this.getTrieNode();
  }

  getTrieNode() {
    return new TrieNode();
  }

  insert(word) {
    let crawler = this.root;
    for (const char of word) {
      const index = char.charCodeAt(0) - 'a'.charCodeAt(0);
      if (crawler.children[index] === null) {
        crawler.children[index] = this.getTrieNode();
      }
      crawler = crawler.children[index];
    }
    crawler.isEndOfWord = true;
  }

  search(word) {
    let crawler = this.root;
    for (const char of word) {
      const index = char.charCodeAt(0) - 'a'.charCodeAt(0);
      if (crawler.children[index] === null) {
        return false;
      }
      crawler = crawler.children[index];
    }
    return crawler !== null && crawler.isEndOfWord;
  }

  startsWith(prefix) {
    let crawler = this.root;
    for (const char of prefix) {
      const index = char.charCodeAt(0) - 'a'.charCodeAt(0);
      if (crawler.children[index] === null) {
        return false;
      }
      crawler = crawler.children[index];
    }
    return true;
  }
}