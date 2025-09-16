class Solution {
public:
    vector<int> replaceNonCoprimes(vector<int>& nums) {
        vector<int> result;
        // processing left to right
        // we touch a number twice, once push to result and once pop from reslt
        // O(2*n) => O(n) * gcd 
        // gcd = log(min(a,b)) = log(x)
        // Tc = O(n) * log(x)
        // Sc = O(1)
        for (int num : nums) {
            while (!result.empty()) {
                int prev = result.back();
                int curr = num;

                int GCD = gcd(prev, curr);
                if (GCD == 1) {
                    break;
                }
                result.pop_back();
                int LCM = prev / GCD * curr;
                num = LCM; // merged number
            }
            result.push_back(num);
        }
        return result;
    }
};