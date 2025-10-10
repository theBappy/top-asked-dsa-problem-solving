
// Tc = O(2^(max m, n))
// Sc = recursion tree max depth(max length of the string or the pattern) => O(n) or O(m)
class Solution {
public:
    
    bool isMatch(string text, string pattern) {
        if (pattern.length() == 0) {
            return text.length() == 0;
        }

        bool first_char_matched = false;
        if(text.length() > 0 && (pattern[0] == text[0] || pattern[0] == '.')) {
            first_char_matched = true;
        }
        if (pattern.length() >= 2 && pattern[1] == '*') {
            return (isMatch(text, pattern.substr(2)) ||
                    (first_char_matched && isMatch(text.substr(1), pattern)));
        } else {
            return first_char_matched && isMatch(text.substr(1), pattern.substr(1));
        }
    }
};


//Approach-2 (Recursion + Memoization)
//T.C : O(m*n)
//S.C : O(m*n)
class Solution {
public:
    int t[21][21]; //O(m.n)
    bool solve(int i, int j, string s, string p) {
        if (j == p.length()) {
            return i == s.length();
        }  
        if(t[i][j] != -1){
            return t[i][j];
        }  
        bool first_char_matched = false;
        if ( i < s.length() && (p[j] == s[i] || p[j] == '.')) {
            first_char_matched = true;
        }
        if(j+1 < p.length() && p[j+1] == '*'){
            bool not_take = solve(i, j + 2, s, p);
            bool take = first_char_matched && solve(i + 1, j, s, p);
            return t[i][j] = not_take || take;
        }
        return t[i][j] = first_char_matched && solve(i + 1, j + 1, s, p);
    }
    
    bool isMatch(string s, string p) {
        memset(t, -1, sizeof(t));
        return solve(0, 0, s, p);
    }
};