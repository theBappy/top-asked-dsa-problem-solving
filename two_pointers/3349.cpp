// Brute force
// Tc = O(n + k)
// Sc = O(1)
class Solution {
public:
    bool isIncreasing(vector<int>& nums, int s, int e) {
        for (int i = s + 1; i < e; i++) {
            if (nums[i] <= nums[i - 1]) { // not increasing
                return false;
            }
        }
        return true;
    }
    bool hasIncreasingSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        for (int start = 0; start + 2 * k <= n; start++) {
            bool first = isIncreasing(nums, start, start + k);
            bool second = isIncreasing(nums, start + k, start + k * 2);
            if (first && second) {
                return true;
            }
        }
        return false;
    }
};

// Optimal
class Solution {
public:
    bool hasIncreasingSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        int currRun = 1;
        int prevRun = 0;
        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i - 1]) {
                currRun++;
            } else {
                // increasing order break
                prevRun = currRun;
                currRun = 1;
            }
            if (currRun >= 2 * k) {
                // can accomodate two sub array in it length >= k
                return true;
            }
            if (min(currRun, prevRun) >= k) {
                return true;
            }
        }
        return false;
    }
};