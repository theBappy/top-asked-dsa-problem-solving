// with stack
class Solution {
public:
    string removeDuplicates(string s) {
        stack<char> st;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (st.empty() || st.top() != s[i]) {
                st.push(s[i]);
            } else {
                st.pop();
            }
        }
        string result = "";
        while (!st.empty()) {
            result += st.top();
            st.pop();
        }
        return result;
    }
};