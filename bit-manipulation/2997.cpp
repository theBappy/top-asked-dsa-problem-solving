// Amazon
// Tc = O(n)
// Sc = O(1)
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int totalXor = 0;
        //O(n)
        for(int &num : nums){
            totalXor ^= num;
        }
        int diff = totalXor ^ k;
        return __builtin_popcount(diff); //log(n)
    }
};