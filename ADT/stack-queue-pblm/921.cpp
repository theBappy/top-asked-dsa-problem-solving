// Meta
// Tc = O(N)

class Solution {
public:
    int minAddToMakeValid(string s) {
        int size = 0;
        int open = 0;
        for (char& ch : s) {
            if (ch == '(') {
                size++;
            } else if (size > 0) {
                size--;
            } else {
                open++;
            }
        }
        return open + size;
    }
};