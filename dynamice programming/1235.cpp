#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> memo;
    int n;

    // Binary search: find the first job whose start >= current job's end
    int getNextIndex(vector<vector<int>>& jobs, int left, int currentEnd) {
        int right = n - 1;
        int result = n; // n means "no next job found"

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (jobs[mid][0] >= currentEnd) {
                result = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return result;
    }

    // Recursive DP
    int solve(vector<vector<int>>& jobs, int i) {
        if (i >= n) return 0; // Base case

        if (memo[i] != -1) return memo[i];

        int nextIndex = getNextIndex(jobs, i + 1, jobs[i][1]);

        int take = jobs[i][2] + solve(jobs, nextIndex);
        int skip = solve(jobs, i + 1);

        return memo[i] = max(take, skip);
    }

    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        n = startTime.size();
        memo.assign(n, -1);

        vector<vector<int>> jobs(n, vector<int>(3));
        for (int i = 0; i < n; i++) {
            jobs[i] = {startTime[i], endTime[i], profit[i]};
        }

        // Sort by start time
        sort(jobs.begin(), jobs.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        return solve(jobs, 0);
    }
};
