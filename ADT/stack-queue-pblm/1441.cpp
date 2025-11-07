class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        int stream = 1;
        int i = 0;
        vector<string> result;
        while (i < target.size() && stream <= n) {
            result.push_back("Push");
            if (target[i] == stream) {
                i++;
            } else {
                result.push_back("Pop");
            }
            stream++;
        }
        return result;
    }
};