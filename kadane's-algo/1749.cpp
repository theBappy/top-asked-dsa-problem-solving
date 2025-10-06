
//Tc = O(n+n) => O(n)
class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        int n = nums.size();
        int currSubSum = nums[0];
        //max sub array sum
        int maxSubSum = nums[0];
        for (int i = 1; i < n; i++) {
            currSubSum = max(nums[i], currSubSum + nums[i]);
            maxSubSum = max(maxSubSum, currSubSum);
        }
        // min sub array sum
        currSubSum = nums[0];
        int minSubSum = nums[0];
        for (int i = 1; i < n; i++) {
            currSubSum = min(nums[i], currSubSum + nums[i]);
            minSubSum = min(minSubSum, currSubSum);
        }
        return max(abs(maxSubSum), abs(minSubSum));
    }
};


//Approach-2 (1 Pass - Kadane's Algorithm for maxsubarrysum and minsybarraysum inside one for loop)
//T.C : O(n)
//S.C : O(1)
class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        int n = nums.size();

        int maxSum = nums[0];
        int minSum = nums[0];

        int currSumMax = nums[0];
        int currSumMin = nums[0];

        for(int i = 1; i < n; i++) {
            currSumMax = max(nums[i], currSumMax + nums[i]);
            maxSum = max(maxSum, currSumMax);


            currSumMin = min(nums[i], currSumMin + nums[i]);
            minSum     = min(minSum, currSumMin);
        }

        return max(maxSum, abs(minSum));


    }
};
