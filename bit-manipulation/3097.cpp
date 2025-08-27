
class Solution {
public:
    void updateWindow(int num, vector<int> & vec, int val){
        for(int i = 0; i < 32; i++){ // O(32) => O(1)
            if((num >> i) & 1){
                vec[i] += val;
            }
        }
    }

    int getDecimalFromBinary(vector<int>& vec){
        int num = 0;
        for(int i = 0; i < 32; i++){ // O(32) => O(1)
            if(vec[i] >0){ // i'th position 1?
                num |= (1 << i);
            }
        }
        return num;
    }

    int minimumSubarrayLength(vector<int>& nums, int k) {
        int n = nums.size();
        int result = INT_MAX;
        int i = 0;
        int j = 0;
        vector<int> vec(32, 0);
        // vec[i] = total number of set bits in i'th position
        // Tc = O(2* n) [twice visiting each element]
        while (j < n) { // O(n)
            updateWindow(nums[j], vec, 1); // adding in current window
            while (i <= j && getDecimalFromBinary(vec) >= k) {
                result = min(result, j - i + 1);
                updateWindow(nums[i], vec, -1); // remove the nums[i] form window
                i++;
            }
            j++;
        }
        return result == INT_MAX ? -1 : result;
    }
};