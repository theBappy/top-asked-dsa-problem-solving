// Top down
// Exponential
// Tc = O(n^k) [but by memoizaion we made it O(n)]
class Solution
{
public:
    int t[10001];
    bool solve(vector<int> &nums, int n, int idx)
    {
        if (idx == n - 1)
            return true;
        if (t[idx] != -1)
            return t[idx];
        for (int i = 1; i <= nums[idx]; i++)
        {
            if (solve(nums, n, idx + i) == true)
                return t[idx] = true;
        }
        return t[idx] = false;
    }
    bool canJump(vector<int> &nums)
    {
        int n = nums.size();
        memset(t, -1, sizeof(t));
        return solve(nums, n, 0);
    }
};

// Bottom up in n^2
class Solution
{
public:
    bool canJump(vector<int> &nums)
    {
        int n = nums.size();

        vector<int> t(n, false);
        // t[i] = True means, you can reach index i

        t[0] = true; // Already at starting index

        for (int i = 1; i < n; i++)
        {
            for (int j = i - 1; j >= 0; j--)
            {
                if (j + nums[j] >= i && t[j])
                { // here t[j] == true means you should be able to reach j also,
                  // then only you can plan to jump(j+nums[i])  from this jth index
                    t[i] = true;
                    break;
                }
            }
        }

        return t[n - 1];
    }
};