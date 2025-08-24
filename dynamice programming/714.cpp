class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int n = prices.size();
        if (n == 0) return 0;

        // Initialize variables to store the maximum profit
        int cash = 0; // Maximum profit when not holding a stock
        int hold = -prices[0]; // Maximum profit when holding a stock

        for (int i = 1; i < n; ++i) {
            // Update cash and hold for the current day
            cash = max(cash, hold + prices[i] - fee); // Sell stock
            hold = max(hold, cash - prices[i]); // Buy stock
        }

        return cash; // Maximum profit at the end of the last day
    }
};
