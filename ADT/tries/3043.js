class TrieNode {
  constructor() {
    this.children = Array(10).fill(null);
  }
}

class Solution {
  constructor() {}

  getTrieNode() {
    return new TrieNode();
  }
  insert(num, root) {
    let crawl = root;
    const numStr = num.toString();
    for (const ch of numStr) {
      const idx = parseInt(ch);
      if (!crawl.children[idx]) {
        crawl.children[idx] = this.getTrieNode();
      }
      crawl = crawl.children[idx];
    }
  }
  search(num, root) {
    let crawl = root;
    const numStr = num.toString();
    let length = 0;
    for (const ch of numStr) {
      const idx = parseInt(ch);
      if (crawl.children[idx]) {
        length++;
        crawl = crawl.children[idx];
      } else {
        break;
      }
    }
    return length;
  }
  longestCommonPrefix(arr1, arr2) {
    const root = this.getTrieNode();
    for (const num of arr1) {
      this.insert(num, root);
    }
    let result = 0;
    for (const num of arr2) {
      result = Math.max(result, this.search(num, root));
    }
    return result;
  }
}
