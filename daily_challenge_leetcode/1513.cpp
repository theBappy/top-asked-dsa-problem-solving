
// Count1 * (count1 + 1) / 2
// Tc = O(n)
// Sc = O(1)
class Solution {
public:
    const int M = 1e9 + 7;
    int numSub(string s) {
        long long result = 0;
        long long count1 = 0;
        for (char ch : s) {
            if (ch == '1') {
                count1++;
            } else {
                result = (result + count1 * (count1 + 1) / 2) % M;
                count1 = 0;
            }
        }
        // adding the last group of 1's
        result = (result + count1 * (count1 + 1) / 2) % M;
        return int(result);
    }
};



//Without long long multiplication worry values
class Solution {
public:
    const int M = 1e9 + 7;
    int numSub(string s) {
        int result = 0;
        int count1 = 0;
        for (char ch : s) {
            if (ch == '1') {
                count1++;
                result = (result + count1) % M;
            } else {
                count1 = 0;
            }
        }
        return result;
    }
};