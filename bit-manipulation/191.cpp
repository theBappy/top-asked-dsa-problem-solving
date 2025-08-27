// Apple, Microsoft, Amazon

// Hamming Weight(Takes the binary representation of an integer and returns the number of 1 bits)

// Facts:
// 1. Number of i'th bit => (num >> i) & 1
// 2. How to unset the right most set bit integer? => n = (n & (n-1))


// Approach-1
class Solution {
public:
    int hammingWeight(int n) {
        int count = 0;
        for(int i = 31; i >= 0; i--){
            if((n>> i) & 1 == 1){
                count++;
            }
        }
        return count;
    }
};


// Approach-2
class Solution {
public:
    int hammingWeight(int n) {
        int count = 0;
        while(n){
            n = n & (n-1); // unsetting the right most set 1->0
            count++;
        }
        return count;
    }
};

// Approach-3
class Solution {
public:
    int hammingWeight(int n) {
        int count = 0;
        while(n){
            count += n % 2;
            n = n / 2;
        }
        return count;
    }
};

// Approach-4
class Solution {
public:
    int hammingWeight(int n) {
        return __builtin_popcount(n);
    }
};

