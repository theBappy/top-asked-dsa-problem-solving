//T.C : O(nlogn) due to sorting
//S.C : O(1)


class Solution {
public:
    int minPairSum(vector<int>& nums) {
        sort(begin(nums), end(nums));
        int maxResult = 0;
        int i = 0, j = nums.size() - 1;
        while (i < j) {
            int sum = nums[i] + nums[j];
            maxResult = max(maxResult, sum);
            i++;
            j--;
        }
        return maxResult;
    }
};