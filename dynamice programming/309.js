/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    const n = prices.length;
    const t = Array.from({ length: n }, () => Array(2).fill(-1));
    
    const solve = (day, canBuy) => {
        if (day >= n) return 0;
        if (t[day][canBuy] !== -1) return t[day][canBuy];
        
        let profit;
        if (canBuy) {
            // Option 1: Buy today
            const buyToday = solve(day + 1, 0) - prices[day];
            // Option 2: Skip
            const skip = solve(day + 1, 1);
            profit = Math.max(buyToday, skip);
        } else {
            // Option 1: Sell today (apply cool-down)
            const sellToday = prices[day] + solve(day + 2, 1);
            // Option 2: Skip
            const skip = solve(day + 1, 0);
            profit = Math.max(sellToday, skip);
        }
        
        t[day][canBuy] = profit;
        return profit;
    };
    
    return solve(0, 1);
};

// Bottom up
// Tc = O(n)
// Sc = O(1)
var maxProfit = function(prices) {
    let n = prices.length;
    if (n <= 1) return 0;

    let hold = -prices[0]; // bought first day
    let sold = 0;          // not possible to sell first day
    let rest = 0;          // no stock, no profit

    for (let i = 1; i < n; i++) {
        let prevHold = hold;
        let prevSold = sold;
        let prevRest = rest;

        hold = Math.max(prevHold, prevRest - prices[i]);
        sold = prevHold + prices[i];
        rest = Math.max(prevRest, prevSold);
    }

    // At the end, we cannot be in "hold" for max profit
    return Math.max(sold, rest);
};
