class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        int n = nums.size();
        int lastOne = -(k + 1);
        for (int i = 0; i < n; i++) {
            if (nums[i] == 1) {
                if (i - lastOne - 1 < k) {
                    return false;
                }
                lastOne = i;
            }
        }
        return true;
    }
};