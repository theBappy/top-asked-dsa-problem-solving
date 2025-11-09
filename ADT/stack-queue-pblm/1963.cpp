
// using stack
// Tc = O(n)
// Sc = O(n)
class Solution {
public:
    int minSwaps(string s) {
        stack<char> st;

        for (char& ch : s) {
            if (ch == '[')
                st.push(ch);
            else if (!st.empty())
                st.pop();
        }

        return (st.size() + 1) / 2;
    }
};


// without using stack
// Tc = O(n)
// Sc = O(1)
class Solution {
public:
    int minSwaps(string s) {
        int size = 0;

        for (char& ch : s) {
            if (ch == '[')
                size++;
            else if (size != 0)
                size--;
        }

        return (size + 1) / 2;
    }
};