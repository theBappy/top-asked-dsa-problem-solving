struct trieNode{
    int countPrefix = 0;
    trieNode* children[26];
};

class Solution {
public:
    trieNode* getTrieNode(){
        trieNode* newNode = new trieNode();
        for(int i = 0; i < 26; i++){
            newNode->children[i] = nullptr;
        }
        newNode->countPrefix = 0;
        return newNode;
    }

    void insert(string& word, trieNode* root){
        trieNode* crawl = root;
        for(char &ch: word){
            int idx = ch - 'a';
            if(!crawl->children[idx]){
                crawl->children[idx] = getTrieNode();
            }
            crawl->children[idx]->countPrefix += 1;
            crawl = crawl->children[idx];
        }
    }

    int getScore(string& word, trieNode* root){
        trieNode* crawl = root;
        int score = 0;
        for(char &ch: word){
            int idx = ch - 'a';
            score += crawl->children[idx]->countPrefix;
            crawl = crawl->children[idx];
        }
        return score;
    }


    vector<int> sumPrefixScores(vector<string>& words) {
        int n = words.size();
        trieNode* root = getTrieNode();
        for(string &word: words){
            insert(word, root);
        }
        vector<int> result(n);
        // result[i] = sum of scores of prefixex of word[i]
        for(int i = 0 ; i < n; i++){
            result[i] = getScore(words[i] , root);
        }
        return result;
    }
};