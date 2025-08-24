

// Recur + Memo
class Solution
{
public:
    int t[5001][2];
    int solve(vector<int> &prices, int day, int n, bool buy)
    {
        if (day >= n)
            return 0;
        if (t[day][buy] != -1)
        {
            return t[day][buy];
        }
        int profit = 0;
        if (buy)
        {
            int selling_day = solve(prices, day + 1, n, false) -
                              prices[day];                    // selling - bought_price
            int buying_day = solve(prices, day + 1, n, true); // buying only
            profit = max({profit, selling_day, buying_day});
        }
        else
        {
            int buying_day = prices[day] + solve(prices, day + 2, n, true);
            int selling_day = solve(prices, day + 1, n, false);
            profit = max({profit, buying_day, selling_day});
        }
        return t[day][buy] = profit;
    }
    int maxProfit(vector<int> &prices)
    {
        int n = prices.size();
        memset(t, -1, sizeof(t));
        bool buy = true; // first day need to buy for having stovk
        return solve(prices, 0, n, buy);
    }
};

// Bottom up
class Solution
{
public:
    int maxP(vector<int> &prices, int &n)
    {
        if (n == 0 || n == 1)
            return 0;
        vector<int> t(n, 0);
        // t[i] = max profit at the end of ith day
        t[0] = 0;
        t[1] = max(prices[1] - prices[0], 0);

        for (int i = 2; i < n; i++)
        {
            t[i] = t[i - 1];

            for (int j = 0; j <= i - 1; j++)
            {

                int prev_profit = j >= 2 ? t[j - 2] : 0;

                t[i] = max(t[i], prices[i] - prices[j] + prev_profit);
            }
        }
        return t[n - 1];
    }
    int maxProfit(vector<int> &prices)
    {
        int n = prices.size();
        return maxP(prices, n);
    }
};