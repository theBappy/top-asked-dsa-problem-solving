

// Tc = O(n.logn)
// Sc = O(1)
class Solution {
public:
    bool check(int num) {
        while (num) {
            if (num % 10 == 0) {
                return false;
            }
            num /= 10;
        }
        return true;
    }
    vector<int> getNoZeroIntegers(int n) {
        for (int a = 1; a <= n - 1; a++) {
            int b = n - a;
            if (check(a) && check(b)) {
                return {a, b};
            }
        }
        return {};
    }
};

// Tc = O(logn)
// Sc = O(1)
class Solution {
public:
    vector<int> getNoZeroIntegers(int n) {
        int a = n;
        int b = 0;
        int placeValue = 1;
        while (n > 1) {
            int take = 1;
            if (n % 10 == 1) {
                take = 2;
            }
            a = a - (take * placeValue);
            b = b + (take * placeValue);
            n = (n - take) / 10; // moving to next digit
            placeValue *= 10;
        }
        return {a, b};
    }
};