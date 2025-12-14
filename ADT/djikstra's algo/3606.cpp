//Approach (Using map and sorting)
//T.C : O(n*l + nlogn) where n = code.size() and l = average length of codes
//S.C : O(n)
class Solution {
public:
    bool checkValidCode(string &code) { // O(l)
        if(code.empty())
            return false;

        for(char &ch : code) {
            if(!isalnum(ch) && ch != '_') {
                return false;
            }
        }

        return true;
    }

    vector<string> validateCoupons(vector<string>& code, vector<string>& businessLine, vector<bool>& isActive) {
        
        unordered_map<string, int> mp = {
            {"electronics", 0},
            {"grocery", 1},
            {"pharmacy", 2},
            {"restaurant", 3}
        };

        vector<pair<int, string>> temp; //{businessLineIntegerValue, code}

        for (int i = 0; i < code.size(); i++) { //O(n * l)
            if (isActive[i] &&
                mp.count(businessLine[i]) &&
                checkValidCode(code[i])) {

                temp.push_back({mp[businessLine[i]], code[i]});
            }
        }

        sort(begin(temp), end(temp)); //O(n.logn)
        vector<string> result;

        for(auto &it : temp) {
            result.push_back(it.second);
        }

        return result;
    }
};
