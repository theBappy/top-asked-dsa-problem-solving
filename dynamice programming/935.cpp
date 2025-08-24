// Recur + Memo
class Solution
{
public:
    int M = 1e9 + 7;
    vector<vector<int>> adj = {
        {4, 6},
        {6, 8},
        {7, 9},
        {4, 8},
        {3, 9, 0},
        {},
        {1, 7, 0},
        {2, 6},
        {1, 3},
        {2, 4}};
    int t[5001][10];
    int solve(int n, int cell)
    {
        if (n == 0)
        {
            return 1;
        }
        if (t[n][cell] != -1)
            return t[n][cell];
        int ans = 0;
        for (int &nextCell : adj[cell])
        {
            ans = (ans + solve(n - 1, nextCell)) % M;
        }
        return t[n][cell] = ans;
    }
    int knightDialer(int n)
    {
        int result = 0;
        memset(t, -1, sizeof(t));
        for (int cell = 0; cell <= 9; cell++)
        {
            result = (result + solve(n - 1, cell)) % M;
        }

        return result;
    }
};

// Bottom Up Approach
// State definition: t[i][j] or t[n][cell] => total number of distinct phone numbers of length i when you are at cell j or total number of distinct phone numbers of length [n] when you are at [cell]
// t[0][cell] will always 1 [base case]
class Solution
{
public:
    int M = 1e9 + 7;
    vector<vector<int>> adj = {{4, 6}, {6, 8}, {7, 9}, {4, 8}, {3, 9, 0}, {}, {1, 7, 0}, {2, 6}, {1, 3}, {2, 4}};

    int knightDialer(int n)
    {
        int result = 0;
        vector<vector<int>> t(n, vector<int>(10));
        for (int cell = 0; cell <= 9; cell++)
        {
            t[0][cell] = 1; // base case
        }
        for (int i = 1; i <= n - 1; i++)
        {
            for (int cell = 0; cell <= 9; cell++)
            {
                int ans = 0;
                for (int &nextCell : adj[cell])
                {
                    ans = (ans + t[i - 1][nextCell]) % M;
                }
                t[i][cell] = ans;
            }
        }
        for (int cell = 0; cell <= 9; cell++)
        {
            result = (result + t[n - 1][cell]) % M;
        }
        return result;
    }
};