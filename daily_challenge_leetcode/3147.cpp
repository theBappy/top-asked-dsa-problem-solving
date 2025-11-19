// Recursion + Memoization
// Tc = O(n)
// Sc = O(n)
class Solution {
public:
    int n;
    int K;

    int solve(int i, vector<int>& energy, vector<int>& t) {
        if (i >= n) 
            return 0;
        
        if (t[i] != INT_MIN)
            return t[i];

        // Take energy at i and then best from (i + k) onwards - Recursion leap of faith
        t[i] = energy[i] + solve(i + K, energy, t);
        
        return t[i];
    }

    int maximumEnergy(vector<int>& energy, int k) {
        n = energy.size();
        K = k;
        vector<int> t(n, INT_MIN);     // Initialize memoization array

        int maxEnergy = INT_MIN;
        for (int i = 0; i < n; i++) {
            maxEnergy = max(maxEnergy, solve(i, energy, t));
        }

        return maxEnergy;
    }
};

// Bottom up
class Solution {
public:
    int maximumEnergy(vector<int>& energy, int k) {
        int n = energy.size();
        vector<int> t(n, 0);
        for (int i = n - 1; i >= 0; i--) {
            if (i + k < n) {
                t[i] = energy[i] + t[i + k];
            } else {
                t[i] = energy[i];
            }
        }
        return *max_element(begin(t), end(t));
    }
};