// Google, Amazon, Yahoo, Microsoft, Meta, MakeMyTrip, Nvidia
// Tc = O(k·L + m·n·4^L)
// Sc = O(k·L + L)

class Solution {
public:
    vector<string> result;          // O(k) space for answers
    int r, c;
    
    // Constant directions → O(1)
    vector<pair<int, int>> directions{{-1, 0},{1, 0},{0, 1},{0, -1}};
    
    struct trieNode {
        bool endOfWord;
        trieNode* children[26];     // Constant size → O(1)
        string word;
    };

    // Creates one trie node → O(1)
    trieNode* getNode() {
        trieNode* temp = new trieNode();
        temp->endOfWord = false;
        
        // Always 26 iterations → O(1)
        for(int i = 0; i < 26; i++) {
            temp->children[i] = NULL;
        }
        
        temp->word = "";
        return temp;
    }

    // Insert one word of length L → O(L)
    void insert(trieNode* root, string str) {
        trieNode* pCrawl = root;
        
        // Loop runs for each character of word → O(L)
        for(char ch : str) {
            if(pCrawl->children[ch - 'a'] == NULL) {
                pCrawl->children[ch - 'a'] = getNode(); // O(1)
            }
            pCrawl = pCrawl->children[ch - 'a']; // O(1)
        }
        
        pCrawl->endOfWord = true;   // O(1)
        pCrawl->word = str;         // O(1)
    }

    // DFS depth ≤ max word length L
    void DFS(vector<vector<char>>& board, int i, int j, trieNode* root) {
        
        // Boundary + visited + trie pruning → O(1)
        if(i < 0 || i >= r || j < 0 || j >= c ||
           board[i][j] == '$' ||
           root->children[board[i][j] - 'a'] == NULL) {
            return;
        }

        // Move down the trie → O(1)
        root = root->children[board[i][j] - 'a'];

        // Found a word → O(1)
        if(root->endOfWord == true) {
            result.push_back(root->word); // amortized O(1)
            root->endOfWord = false;      // prevents duplicates
        }

        char temp = board[i][j];  // O(1)
        board[i][j] = '$';        // O(1)

        // Always 4 directions → O(4) = O(1)
        // BUT recursive calls branch → contributes to 4^L
        for(pair<int, int> p : directions) {
            DFS(board, i + p.first, j + p.second, root);
        }

        board[i][j] = temp;       // Backtracking → O(1)
    }

    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {

        r = board.size();
        c = board[0].size();

        trieNode* root = getNode();   // O(1)

        // Insert k words
        // Total = sum of lengths = O(k · L)
        for(string str : words) {
            insert(root, str);
        }

        // Loop over every cell → O(r · c)
        for(int i = 0; i < r; i++) {
            for(int j = 0; j < c; j++) {

                char ch = board[i][j];

                // O(1) check before DFS
                if(root->children[ch - 'a'] != NULL) {

                    // DFS worst-case → O(4^L)
                    DFS(board, i, j, root);
                }
            }
        }

        return result;
    }
};
