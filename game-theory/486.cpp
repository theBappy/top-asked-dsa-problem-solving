// Approach-1
class Solution {
public:
    int t[23][23];
    int solve(int i, int j, vector<int>& nums){
        if(i > j)
            return 0;
        if(i == j)
            return nums[i];
        if(t[i][j] != -1){
            return t[i][j];
        }
        int take_i = nums[i] + min(solve(i+2, j, nums), solve(i+1, j-1, nums));
        int take_j = nums[j] + min(solve(i+1, j-1, nums), solve(i, j-2, nums));
        return t[i][j] = max(take_i, take_j);
    }
    bool predictTheWinner(vector<int>& nums) {
        memset(t, -1, sizeof(t));
        int n = nums.size();
        int total_score = accumulate(begin(nums), end(nums), 0);
        int p1_score = solve(0, n-1, nums);
        int p2_score = total_score - p1_score;
        return p1_score >= p2_score;
    }
};

// Approach-2
class Solution {
public:
    int t[23][23];
    
    int solve(vector<int>& nums, int i, int j) {
        if (i > j)
            return 0;
        
        if (t[i][j] != -1)
            return t[i][j];
        
        int pick_i = nums[i] - solve(nums, i + 1, j);
        int pick_j = nums[j] - solve(nums, i, j - 1);
        
        t[i][j] = max(pick_i, pick_j);
        return t[i][j];
    }
    
    bool predictTheWinner(vector<int>& nums) {
        int n = nums.size();
        memset(t, -1, sizeof(t));
        return solve(nums, 0, n - 1) >= 0;
    }
};