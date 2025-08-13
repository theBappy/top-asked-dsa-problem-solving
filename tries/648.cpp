class Solution
{
public:
    struct trieNode
    {
        trieNode *children[26];
        bool isEnd;
    };

    trieNode *getNode()
    {
        trieNode *newNode = new trieNode();
        newNode->isEnd = false;

        for (int i = 0; i < 26; i++)
        {
            newNode->children[i] = NULL;
        }
        return newNode;
    }
    trieNode *root;
    void insert(string word)
    {
        trieNode *crawler = root;
        for (int i = 0; i < word.length(); i++)
        {
            int idx = word[i] - 'a';
            if (crawler->children[idx] == NULL)
            {
                crawler->children[idx] = getNode();
            }
            crawler = crawler->children[idx];
        }
        crawler->isEnd = true;
    }

    string search(string word)
    {
        trieNode *crawler = root;
        // O(L) ; l = length
        for (int i = 0; i < word.length(); i++)
        {
            int idx = word[i] - 'a';
            if (crawler->children[idx] == NULL)
            {
                return word;
            }
            crawler = crawler->children[idx];
            if (crawler->isEnd)
            {
                return word.substr(0, i + 1);
            }
        }
        return word;
    }
    string replaceWords(vector<string> &dictionary, string sentence)
    {
        root = getNode();
        // n words
        // l length
        // n * l = total characters of string int the dictionary
        // TC = O(n*l)
        // SC = O(n*l)
        for (string &word : dictionary)
        {
            insert(word);
        }
        stringstream ss(sentence);
        string word;
        string result;
        while (getline(ss, word, ' ')) // O(W * L)
        {
            result += search(word) + ' ';
        }
        result.pop_back();
        return result;
    }
};
