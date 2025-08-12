//T.C : Assuming m is the total number of characters in all words in wordsContainer, the time complexity of the insertTrie method is O(m).
//      Assuming n is the average length of words in wordsQuery, the time complexity of the search method is O(n).
//      T.C for stringIndices can be represented as O(m + n), where m is the total number of characters in wordsContainer and n is the average length of words in wordsQuery.
//S.C : Each node in the trie has an array of 26 pointers (assuming only lowercase English alphabets), 
//      resulting in a space complexity of O(26 * m) for storing all characters of words in wordsContainer. m = total number of characters in all words in wordsContainer.
#include <vector>
#include <string>
using namespace std;

class Solution {
public:

    struct trieNode {
        int idx;
        trieNode* children[26];
    };

    trieNode* getNode(int i) {
        trieNode* temp = new trieNode();
        temp->idx = i;

        for(int i = 0; i<26; i++) {
            temp->children[i] = nullptr;
        }
        return temp;
    }

    void insertTrie(trieNode* pCrawl, int i, vector<string>& wordsContainer) {
        string word = wordsContainer[i];
        int n = word.size();

        for(int j = n-1; j >= 0; j--) {
            int ch_idx = word[j] - 'a';

            if(pCrawl->children[ch_idx] == nullptr) {
                pCrawl->children[ch_idx] = getNode(i);
            }
            pCrawl = pCrawl->children[ch_idx];
            
            // Always set idx to the shortest word index at this node
            if(wordsContainer[pCrawl->idx].size() > n) {
                pCrawl->idx = i;
            }
        }
    }

    int search(trieNode* pCrawl, string &word) {
        int result_idx = pCrawl->idx;
        int n = word.size();

        for(int i = n-1; i >= 0; i--) {
            int ch_idx = word[i]-'a';
            pCrawl = pCrawl->children[ch_idx];
            if(pCrawl == nullptr) {
                return result_idx;
            }
            result_idx = pCrawl->idx;
        }
        return result_idx;
    }

    vector<int> stringIndices(vector<string>& wordsContainer, vector<string>& wordsQuery) {
        int m = wordsContainer.size();
        int n = wordsQuery.size();
        vector<int> result(n);

        // Find the index of the shortest word in wordsContainer
        int minIdx = 0;
        for(int i = 1; i < m; i++) {
            if(wordsContainer[i].size() < wordsContainer[minIdx].size()) {
                minIdx = i;
            }
        }

        trieNode* root = getNode(minIdx);

        for(int i = 0 ; i < m; i++) {
            if(wordsContainer[root->idx].size() > wordsContainer[i].size()) {
                root->idx = i;
            }
            insertTrie(root, i, wordsContainer);
        }

        for(int i = 0; i < n; i++) {
            result[i] = search(root, wordsQuery[i]);
        }

        return result;
    }
};