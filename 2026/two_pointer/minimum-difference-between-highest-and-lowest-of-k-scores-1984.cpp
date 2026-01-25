// Using sorting and two pointers
// T.C : O(nlogn)
// S.C : O(1)

class Solution {
public:
    int minimumDifference(vector<int>& nums, int k) {
        int n = nums.size();

        sort(begin(nums), end(nums));

        int minDiff = INT_MAX;

        int i = 0;
        int j = i+k-1;
        while(j < n) {
            int minElement = nums[i];
            int maxElement = nums[j];

            minDiff = min(minDiff, maxElement - minElement);
            i++;
            j++;
        }

        return minDiff;
    }
};

class Solution {
public:
    int minimumDifference(vector<int>& nums, int k) {
        int n = nums.size();

        sort(begin(nums), end(nums));

        int minDiff = INT_MAX;

        for (int i = k - 1; i < n; i++) {
            int minEl = nums[i - k + 1];
            int maxEl = nums[i];
            minDiff = min(minDiff, maxEl - minEl);
        }

        return minDiff;
    }
};