//T.C : O(n*u), u = unique elements, in worst case  u = n
//S.C : O(u), in worst case u = n
// Gave TLE
class Solution {
public:
    int minOperations(vector<int>& nums) {
        unordered_set<int> st(begin(nums), end(nums)); //O(n) space

        int n = nums.size();

        int ops = 0;

        for(int target : st) { //O(U*n)
            if(target == 0)
                continue;
            
            bool flow = false;
            for(int i = 0; i < n; i++) {
                if(nums[i] == target) {
                    if(!flow) {
                        flow = true;
                        ops++;
                    }
                } else if(nums[i] < target) {
                    flow = false;
                }
            }
        }

        return ops;

        
    }
};


// Monotonic Increasing Stack
//T.C : O(n)
//S.C : O(n)