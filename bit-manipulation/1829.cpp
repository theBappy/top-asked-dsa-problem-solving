// Tc = O(n)
// Sc = O(1)

class Solution {
public:
    vector<int> getMaximumXor(vector<int>& nums, int maximumBit) {
        int n = nums.size();

        vector<int> result(n);

        //step-1 : Find the total xor
        int XOR = 0;
        for(int i = 0; i < n; i++) {
            XOR ^= nums[i];
        }

        //To find flip, first find the mask having all bits set to 1
        int mask = ((1 << maximumBit) - 1);

        for(int i = 0; i < n; i++) {
            int k = XOR ^ mask; //this will give me the flipped value of XOR i.e. my best K
            result[i] = k;

            XOR = (XOR ^ nums[n-1-i]);
        }

        return result;


    }
};
