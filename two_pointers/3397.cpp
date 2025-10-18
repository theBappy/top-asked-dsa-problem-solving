
// Tc = O(n.logn) + n
// Sc = O(1) [some can say O(n) for sorting]
class Solution {
public:
    int maxDistinctElements(vector<int>& nums, int k) {
        int n = nums.size();
        sort(begin(nums), end(nums));
        int count = 0;
        int prev = INT_MIN;
        for (int i = 0; i < n; i++) {
            int minVal = nums[i] - k;
            if (prev < minVal) {
                prev = minVal;
                count++;
            } else if (prev < nums[i] + k) {
                prev = prev + 1;
                count++;
            }
        }
        return count;
    }
};