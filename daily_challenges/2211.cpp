// Tc = O(n^2)

class Solution {
public:
    int triangularSum(vector<int>& nums) {
        while (nums.size() > 1) {
            vector<int> temp;
            for (int i = 0; i < nums.size() - 1; i++) {
                temp.push_back((nums[i] + nums[i + 1]) % 10);
            }
            nums = move(temp);
        }
        return nums[0];
    }
};



class Solution {
public:
    int triangularSum(vector<int>& nums) {
        int n = nums.size();
        for (int size = n - 1; size >= 1; size--) {
            for (int i = 0; i < size; i++) {
                nums[i] = (nums[i] + nums[i + 1]) % 10;
            }
        }
        return nums[0];
    }
};