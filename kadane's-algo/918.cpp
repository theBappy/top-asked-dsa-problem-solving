
// Tc = O(n)
// Sc = O(1)
class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int n   = nums.size();
        int SUM = accumulate(begin(nums), end(nums), 0);
        
        int k_sum_min = nums[0];
        int min_sum   = nums[0];
        
        int k_sum_max = nums[0];
        int max_sum   = nums[0];
        
        for(int i = 1; i<nums.size(); i++) {
            
            min_sum   = min(nums[i]+min_sum, nums[i]);
            k_sum_min = min(k_sum_min, min_sum);
            
            max_sum = max(nums[i]+max_sum, nums[i]);
            k_sum_max = max(k_sum_max, max_sum);
         
        }
        
        int circular_sum = SUM - k_sum_min;
        
        if(k_sum_max > 0) {
            return max(k_sum_max, circular_sum);
        }
        
        return k_sum_max;
        
    }
};