
// Top-down
class Solution {
public:
    int t[46];
    int solve(int n){
        if(n < 0)
            return 0;
        if(t[n] != -1)
            return t[n];
        if(n == 0)
            return 1;
        int one_step = solve(n-1);
        int two_step = solve(n-2);
        return t[n] = one_step + two_step; 
    }
    int climbStairs(int n) {
        memset(t, -1, sizeof(t));
        return solve(n);
    }
};

// Bottom-up
// array[i] = no of ways to climb i stairs
class Solution {
public:
    int climbStairs(int n) {
        if(n == 1 || n == 2 || n == 3)
            return n;
        vector<int> stair(n+1);
        stair[0] = 0;
        stair[1] = 1;
        stair[2] = 2;
        // only need (i - 1) and (i - 2)
        for(int i = 3; i <= n; i++){
            stair[i] = stair[i-1] + stair[i-2];
        }
        return stair[n];
    }
};

class Solution {
public:
    int climbStairs(int n) {
        if(n == 1 || n == 2)
            return n;
        int a = 1;
        int b = 2;
        int c = 3;
        for(int i = 3; i <= n; i++){
            c = b + a;
            int temp_b = b;
            b = c;
            a = temp_b;
        }
        return c;
    }
};