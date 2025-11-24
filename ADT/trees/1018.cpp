// How to left shift???

// simply multiply by 2
// One extra space for multiply -> nums[i] need to placed in this extra add nums[i]
class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& nums) {
        int n = nums.size();
        vector<bool> result(n);

        int remain = 0;
        for (int i = 0; i < n; i++) {
            remain = (remain * 2 + nums[i]) % 5;
            result[i] = (remain == 0);
        }
        return result;
    }
};

