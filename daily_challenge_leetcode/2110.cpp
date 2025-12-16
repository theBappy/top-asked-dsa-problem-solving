//T.C : O(n)
//S.C : O(1)

class Solution {
public:
    long long getDescentPeriods(vector<int>& prices) {
        long long result = 1;
        long long count = 1;
        for (int i = 1; i < prices.size(); i++) {
            if (prices[i - 1] - prices[i] == 1) {
                count++;
            } else {
                count = 1;
            }
            result += count;
        }
        return result;
    }
};