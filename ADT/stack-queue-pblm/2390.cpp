// Microsoft

// stack
class Solution {
public:
    string removeStars(string s) {
        stack<char> st;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '*')
                st.pop();
            else
                st.push(s[i]);
        }
        string result = "";
        while (!st.empty()) {
            result.push_back(st.top());
            st.pop();
        }
        reverse(begin(result), end(result));
        return result;
    }
};

// string
class Solution {
public:
    string removeStars(string s) {
        string result = "";
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '*')
                result.pop_back();
            else
                result.push_back(s[i]);
        }
        return result;
    }
};


// 2 pointers
class Solution {
public:
    string removeStars(string s) {
        vector<char> ch(s.size());
        int j = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '*') {
                j--;
            } else {
                ch[j++] = s[i];
            }
        }

        string result = "";
        for (int i = 0; i < j; i++) {
            result.push_back(ch[i]);
        }

        return result;
    }
};
