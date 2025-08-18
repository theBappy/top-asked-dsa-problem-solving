// Top down(recursion+memoization)
class Solution {
public:
    int M = 1e9+7;
    int t[1001];
    int solve(int n){
        if(n == 1 || n == 2)
            return n;
        if(t[n] != -1)
            return t[n];
        if(n == 3)
            return 5;
        return t[n] = (2*solve(n-1) % M + solve(n-3) % M) % M;
    }
    int numTilings(int n) {
        memset(t, -1, sizeof(t));
        return solve(n);
    }
};

// Bottom Up
class Solution {
public:
    int M = 1000000007;
    int numTilings(int n) {
        if(n == 1 || n == 2)
            return n;

        vector<int> t(n+1, 0);
        
        t[1] = 1;
        t[2] = 2;
        t[3] = 5;
        
        for(int i = 4; i<=n; i++) {
            t[i] = (2*t[i-1]%M + t[i-3]%M) % M;
        }
        
        return t[n];
        
        
    }
}; 