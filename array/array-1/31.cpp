// Tc = O(n) [as each step scans at most the full array once]
// Sc = O(1)

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        // first find the element to swap
        // O(n)
        int swap_index = -1;
        for (int i = n - 1; i > 0; i--) {
            if (nums[i] > nums[i - 1]) {
                swap_index = i - 1;
                break;
            }
        }
        // O(n) => finding successor
        if (swap_index != -1) {
            int just_greater = swap_index;
            for (int j = n - 1; j >= swap_index + 1; j--) {
                if (nums[j] > nums[swap_index]) {
                    just_greater = j;
                    break;
                }
            }
            // O(1)
            swap(nums[swap_index], nums[just_greater]);
        }
        // O(n) [single pass reversing the suffix]
        reverse(nums.begin() + swap_index + 1, nums.end());
    }
};