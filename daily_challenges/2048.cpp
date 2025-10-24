//Approach-1 (Simple Simulation)
//T.C : O(L-n), where L = 1224444
//S.C : O(1)
class Solution {
public:
    bool balanced(int num) {
        vector<int> freq(10);
        while(num > 0) {
            int digit = num%10;
            freq[digit]++;
            num /= 10;
        }
        for(int d = 0; d < 10; d++) {
            if(freq[d] != 0 && freq[d] != d)
                return false;
        }
        return true;
    }
    int nextBeautifulNumber(int n) {
        for(int num = n+1; num <= 1224444; num++) {
            if(balanced(num)) {
                return num;
            }
        }
        return -1;
    }
};