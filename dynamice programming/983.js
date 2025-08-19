/**
 * @param {number[]} days
 * @param {number[]} costs
 * @return {number}
 */
var mincostTickets = function(days, costs) {
 const n = days.length;
    const t = Array(366).fill(-1); // Memoization array

    function solve(i) {
        if (i >= n) {
            return 0; // No more travel days
        }
        if (t[i] !== -1) {
            return t[i];
        }

        // 1-day pass
        const cost_1 = costs[0] + solve(i + 1);

        // 7-day pass
        let j = i;
        const max_day_7 = days[i] + 7;
        while (j < n && days[j] < max_day_7) {
            j++;
        }
        const cost_7 = costs[1] + solve(j);

        // 30-day pass
        j = i;
        const max_day_30 = days[i] + 30;
        while (j < n && days[j] < max_day_30) {
            j++;
        }
        const cost_30 = costs[2] + solve(j);

        // Store the minimum cost in the memoization array
        t[i] = Math.min(cost_1, cost_7, cost_30);
        return t[i];
    }

    return solve(0);
};


// Bottom Up
class Solution{
class Solution {
    mincostTickets(days, costs) {
        const st = new Set(days);
        const last_day = days[days.length - 1];
        const t = new Array(last_day + 1).fill(0);
        t[0] = 0;

        for (let i = 1; i <= last_day; i++) {
            if (!st.has(i)) {
                t[i] = t[i - 1];
                continue;
            }
            t[i] = Infinity;
            const d_1 = costs[0] + t[Math.max(i - 1, 0)];
            const d_7 = costs[1] + t[Math.max(i - 7, 0)];
            const d_30 = costs[2] + t[Math.max(i - 30, 0)];
            t[i] = Math.min(d_1, d_7, d_30);
        }
        return t[last_day];
    }
}}