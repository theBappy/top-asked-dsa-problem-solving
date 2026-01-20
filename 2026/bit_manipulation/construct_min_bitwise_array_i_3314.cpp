//T.C : O(n * m), m = maximum number in nums
//S.C : O(1)
class Solution {
public:
    vector<int> minBitwiseArray(vector<int>& nums) {
        vector<int> result;
        for (int& num : nums) {
            bool found = false;
            for (int x = 0; x < num; x++) {
                if ((x | (x + 1)) == num) {
                    result.push_back(x);
                    found = true;
                    break;
                }
            }
            if (!found) {
                result.push_back(-1);
            }
        }
        return result;
    }
};

//T.C : O(n)
//S.C : O(1)
class Solution {
public:
    vector<int> minBitwiseArray(vector<int>& nums) {
        vector<int> result;


        for(int &num : nums) {
            if(num == 2) {
                result.push_back(-1);
                continue;
            }

            bool found = false;
            for(int j = 1; j < 32; j++) {
                if((num & (1 << j)) > 0) { //set bit
                    continue;
                }

                //we found an unset bit at jth position
                result.push_back((num ^ (1 << (j-1)))); //set the first set bit to 0
                found = true;
                break;
            }

            if(!found)
                result.push_back(-1);
        }

        return result;
    }
};
