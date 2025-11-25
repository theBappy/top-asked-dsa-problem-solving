// Tc = O(k)
// Sc = O(1)

class Solution {
public:
    int smallestRepunitDivByK(int k) {
        if (k == 1) {
            return 1;
        }
        int num = 0;
        for (int length = 1; length <= k; length++) {
            num = (num * 10 + 1) % k;
            if (num == 0) {
                return length;
            }
        }
        return -1;
    }
};