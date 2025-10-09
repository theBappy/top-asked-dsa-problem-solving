// Tc = O(m*n)
// Sc = O(n)

class Solution {
public:
    long long minTime(vector<int>& skill, vector<int>& mana) {
        int n = skill.size(), m = mana.size();
        vector<long long> finishTime(n, 0); // finishTime[i] = when wizard i finishes current potion

        for (int j = 0; j < m; ++j) {
            finishTime[0] += 1LL * mana[j] * skill[0];

            for (int i = 1; i < n; ++i)
                finishTime[i] = max(finishTime[i], finishTime[i - 1]) + 1LL * mana[j] * skill[i];

            for (int i = n - 1; i > 0; --i)
                finishTime[i - 1] = finishTime[i] - 1LL * mana[j] * skill[i];
        }
        return finishTime[n-1];
    }
};