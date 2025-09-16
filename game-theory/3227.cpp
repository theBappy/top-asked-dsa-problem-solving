class Solution {
public:
    bool doesAliceWin(string s) {
        auto lambda = [](char ch) {
            return string("aeiou").find(ch) != string::npos;
        };
        return any_of(begin(s), end(s), lambda);
    }
};