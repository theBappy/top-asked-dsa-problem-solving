class TrieNode {
  constructor() {
    this.children = {};
    this.endOfWord = false;
    this.word = "";
  }
}

class WordSearch {
  constructor() {
    this.result = [];
    this.directions = [[-1, 0], [1, 0], [0, 1], [0, -1]];
  }

  insert(root, word) {
    let node = root;
    for (const ch of word) {
      if (!node.children[ch]) {
        node.children[ch] = new TrieNode();
      }
      node = node.children[ch];
    }
    node.endOfWord = true;
    node.word = word;
  }

  findWords(board, words) {
    const rows = board.length;
    const cols = board[0]?.length || 0;

    // Build the Trie
    const root = new TrieNode();
    for (const word of words) {
      this.insert(root, word);
    }

    // DFS function
    const dfs = (i, j, node) => {
      // Boundary checks and visited check
      if (i < 0 || i >= rows || j < 0 || j >= cols || 
          board[i][j] === '$' || !node.children[board[i][j]]) {
        return;
      }

      const currChar = board[i][j];
      const nextNode = node.children[currChar];
      
      // If we found a word
      if (nextNode.endOfWord) {
        this.result.push(nextNode.word);
        nextNode.endOfWord = false; // Avoid duplicates
      }

      // Mark as visited
      board[i][j] = '$';

      // Explore all 4 directions
      for (const [di, dj] of this.directions) {
        dfs(i + di, j + dj, nextNode);
      }

      // Backtrack
      board[i][j] = currChar;
    };

    // Search the board
    for (let i = 0; i < rows; i++) {
      for (let j = 0; j < cols; j++) {
        if (root.children[board[i][j]]) {
          dfs(i, j, root);
        }
      }
    }

    return this.result;
  }
}

// Example usage:
const board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
];
const words = ["oath","pea","eat","rain"];

const ws = new WordSearch();
console.log(ws.findWords(board, words)); // Output: ["oath","eat"]
