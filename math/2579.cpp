// Google, Meta, Apple

// 1 + 2n(n-1)
// n = 4, 1 + 2*4(4-1) => 1 + 24 => 25
// Tc = O(1)
// Sc = O(1)
class Solution {
public:
    long long coloredCells(int n) {
        return 1 +(2 * (long long)(n-1) * n);
    }
};




// Tc = O(n)
class Solution {
public:
    long long coloredCells(int n) {
        int t = 1;
        long long cells = 1;
        while(t <= n){
            cells += (4 * (t - 1));
            t++;
        }
        return cells;
    }
};