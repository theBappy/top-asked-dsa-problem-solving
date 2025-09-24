//T.C : O(m+n)
//S.C : O(m+n)

class Solution {
public:
    vector<string> getTokens(string version) {
        stringstream ss(version);
        string token = "";
        vector<string> tokens;
        while (getline(ss, token, '.')) {
            tokens.push_back(token);
        }
        return tokens;
    }
    int compareVersion(string version1, string version2) {
        // space = O(m+n)
        vector<string> v1 = getTokens(version1); // O(m)
        vector<string> v2 = getTokens(version2); // O(n)

        int m = v1.size();
        int n = v2.size();
        int i = 0;
        while(i < m || i < n) {
            int a = i < m ? stoi(v1[i]) : 0 ;
            int b = i < n ? stoi(v2[i])  : 0 ;
            if (a < b) {
                return -1;
            } else if (a > b) {
                return 1;
            } else {
                i++;
            }
        }
        return 0; // equal version
    }
};