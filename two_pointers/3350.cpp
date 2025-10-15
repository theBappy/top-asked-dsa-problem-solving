// Tc = O(n)
// Sc = O(1)

class Solution {
public:
    int maxIncreasingSubarrays(vector<int>& nums) {
        int n = nums.size();
        int prevRun = 0;
        int currRun = 1;
        int K = 0;
        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i - 1]) {
                currRun++;
            } else {
                prevRun = currRun;
                currRun = 1;
            }
            K = max(K, currRun / 2);
            K = max(K, min(prevRun, currRun));
        }
        return K;
    }
};