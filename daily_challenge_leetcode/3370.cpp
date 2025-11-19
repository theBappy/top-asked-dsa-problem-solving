class Solution {
public:
    bool isAllBitsSet(int x){
        return (x & (x+1)) == 0;
    }
    int smallestNumber(int n) {
        int result = n;
        while(!isAllBitsSet(result)){
            result++;
        }
        return result;
    }
};

class Solution {
public:
    int smallestNumber(int n) {
        int result = 1;
        while (result < n) {
            result = 2 * result + 1;
        }
        return result;
    }
};


class Solution {
public:
    int smallestNumber(int n) {
        int bits = log2(n) + 1;
        return (1 << bits) - 1;
    }
};