

// Approach - 1

class Solution {
public:
    int xorAllNums(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();

        unordered_map<int, long> mp;
        for(int &num: nums1){
            mp[num] += n;
        }
        for(int &num: nums2){
            mp[num] += m;
        }

        int result = 0;
        for(auto &it: mp){
            int num = it.first;
            int freq = it.second;
            if(freq % 2 != 0){
                result ^= num;
            }
        }
        return result;
    }
};



class Solution {
public:
    int xorAllNums(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();

        int XOR = 0;
        if(m % 2 != 0){
            for(int &num: nums2){
                XOR ^= num;
            }
        }

        if(n % 2 != 0){
            for(int &num: nums1){
                XOR ^= num;
            }
        }
        return XOR;
    }
};
