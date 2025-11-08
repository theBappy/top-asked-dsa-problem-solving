
// Tc = O(n)
// Sc = O(n) but if vector space needs only
class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        stack<int> st;
        for (int& a : asteroids) {
            while (!st.empty() && a < 0 && st.top() > 0) {
                int sum = a + st.top();
                if (sum < 0) {
                    st.pop();
                } else if (sum > 0) {
                    a = 0;
                } else {
                    st.pop();
                    a = 0;
                }
            }
            if (a != 0) {
                st.push(a);
            }
        }
        int s = st.size();
        vector<int> result(s);
        int i = s - 1;
        while (!st.empty()) {
            result[i] = st.top();
            st.pop();
            i--;
        }
        return result;
    }
};