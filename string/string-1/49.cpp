// with sorting
// Tc = O(k.logk) -> sorting + n (iterating in a given string)
// Tc = O(n*k*logk)
//S.C : O(n*k)
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        int n = strs.size();
        vector<vector<string>> result;
        unordered_map<string, vector<string>> mp;
        //n
        for (int i = 0; i < n; i++) { //k.logk
            string temp = strs[i];
            sort(begin(temp), end(temp));
            mp[temp].push_back(strs[i]);
        }
        for (auto it : mp) {
            result.push_back(it.second);
        }
        return result;
    }
};

// without sorting
// Tc = O(N*(k+26)) => O(N*K)

class Solution {
public:
    
    string generate(string &s) {
        int count[26] = {0};
        
        for(char &ch : s) {
            count[ch-'a']++;
        }
        
        string new_s;
        
        for(int i = 0; i<26; i++) {
            
            if(count[i] > 0) {
                new_s += string(count[i], i+'a');
            }
        }
        
        return new_s;
    }
    
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        
        for(string &s : strs) {
            string new_s = generate(s);
            
            mp[new_s].push_back(s);
        }
        
        vector<vector<string>> result;
        for(auto &it : mp) {
            result.push_back(std::move(it.second));
        }
        
        return result;
        
    }
};
