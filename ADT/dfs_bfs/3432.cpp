// Two pass solution
// Tc = O(n + n) [for total sum and for leftSum-rightSum] => O(n)
// Sc = O(1)
class Solution {
public:
    int countPartitions(vector<int>& nums) {
        int n = nums.size();
        int sum = accumulate(begin(nums), end(nums), 0);
        int leftSum = 0;
        int result = 0;
        for (int i = 0; i < n - 1; i++) {
            leftSum += nums[i];
            int rightSum = sum - leftSum;
            if ((leftSum - rightSum) % 2 == 0) {
                result++;
            }
        }
        return result;
    }
};



// One pass solution
// Tc = O(n) [only for total sum]
// Sc = O(1)
class Solution {
public:
    int countPartitions(vector<int>& nums) {
        int n = nums.size();
        int sum = accumulate(begin(nums), end(nums), 0);
        if (sum % 2 == 0)
            return n - 1;
        return 0;
    }
};

