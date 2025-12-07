//T.C : O(high-low)
//S.C : O(1)
class Solution {
public:
    int countOdds(int low, int high) {
        int count = 0;
        low = low % 2 ? low : low + 1;
        for (int num = low; num <= high; num += 2) {
            count++;
        }
        return count;
    }
};

// Tc = O(1)
// Sc = O(1)
class Solution {
public:
    int countOdds(int low, int high) {
        if (low % 2 == 0)
            low++;
        if (high % 2 == 0)
            high--;
        return (high - low) / 2 + 1;
    }
};


// Tc = O(1)
// Sc = O(1)
class Solution {
public:
    int countOdds(int low, int high) {
        return (high + 1) / 2 - (low) / 2;
    }
};