
// gcd Tc, = log(max(element))
// Tc = O(n*n*log(max(element)))
// Sc = O(1)

class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();
        int count1 = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 1)
                count1++;
        }
        if (count1 > 0) {
            return n - count1;
        }
        int minOps = INT_MAX;
        for (int i = 0; i < n - 1; i++) {
            int GCD = nums[i];
            for (int j = i + 1; j < n; j++) {
                GCD = gcd(GCD, nums[j]);
                if (GCD == 1) {
                    minOps = min(minOps, j - i);
                    break;
                }
            }
        }
        if(minOps == INT_MAX){
            return -1;
        }
        return minOps + (n-1);
    }
};