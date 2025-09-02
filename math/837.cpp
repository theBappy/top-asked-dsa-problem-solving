// Google

// Brute force gave T.L.E
class Solution {
public:
    double new21Game(int n, int k, int maxPts) {
        vector<double> P(n + 1, 0.0);
        // P[i] = probability of getting score = i
        P[0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int card = 1; card <= maxPts; card++) {
                // probability of score card = 1/maxPts
                // remaining score = P[i - card]
                if (i-card >= 0 && i-card < k) {
                    P[i] = P[i] + P[i - card] / maxPts;
                }
            }
        }
        // k to n probability add
        return accumulate(begin(P) + k, end(P), 0.0);
    }
};


//Optimal Approach
// Tc = O(n)
class Solution {
public:
    double new21Game(int n, int k, int maxPts) {
        vector<double> P(n + 1, 0.0);
        P[0] = 1;
        double currPorbSum = (k == 0) ? 0 : 1;
        for (int i = 1; i <= n; i++) {
            P[i] = currPorbSum / maxPts;
            if (i < k)
                currPorbSum += P[i];
            if (i - maxPts >= 0 && i - maxPts < k)
                currPorbSum -= P[i - maxPts];
        }
        return accumulate(begin(P) + k, end(P), 0.0);
    }
};