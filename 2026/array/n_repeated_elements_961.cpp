// Using Hashset
// T.C : O(n)
// S.C : O(n)
class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        unordered_set<int> st;
        for (int  &num : nums) {
            if (st.count(num))
                return num;
            st.insert(num);
        }
        return -1;
    }
};

// Using 10^4 Size array ~ Constant Space
// T.C : O(n)
// S.C : O(10^4) => O(1)
class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        vector<int> freq(10001, 0);
        for(int &num: nums){
            freq[num]++;
            if(freq[num] > 1)
                return num;
        }
        return -1;
    }
};


// Without using any extra variable to store space - True Constant Space
// T.C : O(n)
// S.C : O(1)
class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        int n = nums.size();
        
        for(int i = 2; i<n; i++) {
            if(nums[i] == nums[i-1] || nums[i] == nums[i-2])
                return nums[i];
        }
        
        return nums[n-1]; //or, nums[0]
    }
};