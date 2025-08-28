// Google, Twitter


// Approach-1
// Any number to represent in binary needs maximum number of bits => log2(n)
// Tc , Sc = O(log(n))
class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        int shiftCount = 0;
        while(left != right){
            //longest common prefix
            left = (left >> 1);
            right = (right >> 1);
            shiftCount++;
        }
        return left << shiftCount;
    }
};

// Approach-2
// Clears the right most set bit => n & (n-1)
// Helps to find number of set bits => n & (n-1)
// Check power of 2: n > 0 && (n & (n-1))
// Tc = O(log(n))
class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        while(right > left){
            right = right & (right - 1);
        }
        return right;
    }
};