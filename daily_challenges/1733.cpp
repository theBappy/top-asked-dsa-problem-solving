class Solution {
public:
    int minimumTeachings(int n, vector<vector<int>>& languages,
                         vector<vector<int>>& friendships) {
        unordered_set<int> sadUsers;
        //O(F*L)
        for (auto &friends : friendships) {
            int u = friends[0] - 1; // convert this to 0 base indexing
            int v = friends[1] - 1;

            unordered_set<int> langSet(begin(languages[u]), end(languages[u]));

            bool canTalk = false;
            for (int lang : languages[v]) {
                if (langSet.count(lang)) {
                    canTalk = true;
                    break;
                }
            }
            if (!canTalk) {
                sadUsers.insert(u);
                sadUsers.insert(v);
            }
        }
        // find max known language among sad users
        vector<int> language(n + 1, 0);
        int mostKnownLang = 0;
        for (int user : sadUsers) {
            for (int lang : languages[user]) {
                language[lang]++;
                mostKnownLang = max(mostKnownLang, language[lang]);
            }
        }
        return sadUsers.size() - mostKnownLang;
    }
};