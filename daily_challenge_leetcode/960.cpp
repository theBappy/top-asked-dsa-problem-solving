

// Feynman Technique to deep learning and understandings

//Approach - Using LIS
//T.C : O(cols*cols*rows)
//S.C : O(cols)
class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int rows = strs.size();
        int cols = strs[0].length();

        vector<int> dp(cols, 1);
        //dp[i] = LIS ending at index i

        int LIS = 1;

        //Khandani LIS Pattern
        for(int i = 0; i < cols; i++) {
            for(int j = 0; j < i; j++) {

                bool valid = true;
                for(int k = 0; k < rows; k++) {
                    if(strs[k][j] > strs[k][i]) {
                        valid = false;
                        break;
                    }
                }

                if(valid) {
                    dp[i] = max(dp[i], dp[j]+1);
                }

            }

            LIS = max(LIS, dp[i]);
        }

        return cols - LIS;

    }
};
