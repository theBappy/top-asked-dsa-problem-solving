// Amazon, Meta
// Tc = O(n)
// Sc = O(n) [stack]

class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int n = nums.size();
        int num3 = INT_MIN;
        stack<int> st;
        for (int i = n - 1; i >= 0; i--) {
            if (nums[i] < num3) {
                return true;
            }
            while (!st.empty() && st.top() < nums[i]) {
                num3 = st.top();
                st.pop();
            }
            st.push(nums[i]);
        }
        return false;
    }
};