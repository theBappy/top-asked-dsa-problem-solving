
// Tc = O(n)
// Sc = O(32) => O(1)
class Solution {
public:
    vector<int> smallestSubarrays(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n);
        vector<int> setBitIndex(32, -1);
        // setBitIndex[j] = i, it means that j'th bit can be set via element at
        // index i in nums
        for (int i = n - 1; i >= 0; i--) { //O(n)
            // nums[i] = binary rep
            int endIndex = i;
            for (int j = 0; j < 32; j++) { //O(32) => O(1)
                if (!(nums[i] & (1 << j))) { // if j'th bit not set
                    if (setBitIndex[j] != -1) {
                        endIndex = max(endIndex, setBitIndex[j]);
                    }
                } else {
                    setBitIndex[j] = i;
                }
            }
            result[i] = endIndex - i + 1;
        }
        return result;
    }
};