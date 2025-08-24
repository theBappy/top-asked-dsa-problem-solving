

class Solution {
public:
    vector<int> longestObstacleCourseAtEachPosition(vector<int>& obstacles) {
        int n = obstacles.size();
        vector<int> LIS;
        vector<int> result(n);

        for (int i = 0; i < n; i++) {
            int idx =
                upper_bound(begin(LIS), end(LIS), obstacles[i]) - begin(LIS);
            if (idx == LIS.size()) {
                LIS.push_back(obstacles[i]);
            } else {
                LIS[idx] = obstacles[i]; // idx + 1 length of subseq
            }
            result[i] = idx + 1;
        }
        return result;
    }
};