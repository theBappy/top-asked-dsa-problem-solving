//Recur + Memo
// Tc = O(n *(forget-delay))
// Sc = O(n)
class Solution {
public:
    int M = 1e9 + 7;
    vector<int> t;
    // this will return total number of people by day "day"
    int solve(int day, int delay, int forget) {
        if (day == 1) {
            return 1;
        }
        if (t[day] != -1) {
            return t[day];
        }
        int result = 0;
        for (int prev = day - forget + 1; prev <= day - delay; prev++) {
            if (prev > 0) {
                result = (result + solve(prev, delay, forget)) % M;
            }
        }
        t[day] = result;
        return t[day];
    }
    int peopleAwareOfSecret(int n, int delay, int forget) {
        int total = 0;
        t.assign(n + 1, -1);
        for (int day = n - forget + 1; day <= n; day++) {
            if (day > 0) {
                total = (total + solve(day, delay, forget)) % M;
            }
        }
        return total;
    }
};

// Bottom Up
// t[day] = no of people will know the secret on day n

class Solution {
public:
    int M = 1e9 + 7;
    int peopleAwareOfSecret(int n, int delay, int forget) {
        vector<int> t(n + 1);
        t[1] = 1;
        for (int day = 2; day <= n; day++) {
            long long count = 0;
            for (int prev = day - forget + 1; prev <= day - delay; prev++) {
                if (prev > 0) {
                    count = (count + t[prev]) % M;
                }
            }
            t[day] = count;
        }
        int result = 0;
        for (int day = n - forget + 1; day <= n; day++) {
            if (day > 0) {
                result = (result + t[day]) % M;
            }
        }
        return result;
    }
};


// Optimizing bottom-up
class Solution {
public:
    int M = 1e9 + 7;
    int peopleAwareOfSecret(int n, int delay, int forget) {
        vector<int> t(n + 1);
        t[1] = 1;
        int count = 0;
        for (int day = 2; day <= n; day++) {
            if (day - delay > 0) {
                count = (count + t[day - delay]) % M;
            }
            if (day - forget > 0) {
                count = (count - t[day - forget] + M) % M;
            }
            t[day] = count;
        }
        int result = 0;
        for (int day = n - forget + 1; day <= n; day++) {
            if (day > 0) {
                result = (result + t[day]) % M;
            }
        }
        return result;
    }
};