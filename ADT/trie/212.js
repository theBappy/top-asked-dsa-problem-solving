var findWords = function (board, words) {

    const result = [];
    const r = board.length;
    const c = board[0].length;

    const directions = [
        [-1, 0],
        [1, 0],
        [0, 1],
        [0, -1]
    ];

    // Trie node structure
    function TrieNode() {
        this.endOfWord = false;
        this.children = {};   // char -> TrieNode
        this.word = "";
    }

    // Create root
    const root = new TrieNode();

    // Insert words into Trie → O(k · L)
    for (const word of words) {
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

    // DFS (same logic as C++ / Python)
    function DFS(i, j, node) {

        if (
            i < 0 || i >= r ||
            j < 0 || j >= c ||
            board[i][j] === '$' ||
            !node.children[board[i][j]]
        ) {
            return;
        }

        node = node.children[board[i][j]];

        if (node.endOfWord) {
            result.push(node.word);
            node.endOfWord = false; // avoid duplicates
        }

        const temp = board[i][j];
        board[i][j] = '$';         // mark visited

        for (const [dx, dy] of directions) {
            DFS(i + dx, j + dy, node);
        }

        board[i][j] = temp;        // backtrack
    }

    // Start DFS from each cell → O(r · c)
    for (let i = 0; i < r; i++) {
        for (let j = 0; j < c; j++) {
            if (root.children[board[i][j]]) {
                DFS(i, j, root);
            }
        }
    }

    return result;
};
