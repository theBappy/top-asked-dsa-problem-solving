// Google
// Tc = O( m · log R ) [no of battery for possible function * logR for binary search]
// Sc = O(1)
class Solution {
public:
    typedef long long ll;

    bool possible(vector<int>& batteries, ll mid, int n) { //m
        ll target = mid * n;
        ll sum = 0;
        for (ll b : batteries) {
            sum += min(b, mid);
            if (sum >= target) return true;
        }
        return false;
    }

    long long maxRunTime(int n, vector<int>& batteries) {
        ll sum = 0;
        for (int b : batteries) sum += b;

        ll l = 0;
        ll r = sum / n; 
        ll ans = 0;
        while (l <= r) { //log(k)
            ll mid = l + (r - l) / 2;
            if (possible(batteries, mid, n)) {
                ans = mid;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return ans;
    }
};
