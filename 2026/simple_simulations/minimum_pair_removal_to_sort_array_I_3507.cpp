// Simple Simulation
//T.C : O(n^2)
//S.C : O(1)

class Solution {
public:
    int minPairSum(vector<int>& nums) {
        int minSum = INT_MAX;
        int index = -1;

        for(int i = 0; i < nums.size()-1; i++) {
            if(nums[i] + nums[i+1] < minSum) {
                index = i;
                minSum = nums[i] + nums[i+1];
            }
        }

        return index;
    }
    int minimumPairRemoval(vector<int>& nums) {
        int operations = 0;

        while(!is_sorted(begin(nums), end(nums))) {
            int index = minPairSum(nums);

            nums[index] = nums[index] + nums[index+1];

            nums.erase(begin(nums) + index + 1);

            operations++;
        }

        return operations;
    }
};