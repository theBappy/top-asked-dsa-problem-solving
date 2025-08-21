/**
 * @param {number[][]} piles
 * @param {number} k
 * @return {number}
 */
var maxValueOfCoins = function (piles, k) {
        const n = piles.length;
        const t = Array.from({ length: n + 1 }, () => Array(k + 1).fill(-1));

        const solve = (i, k) => {
            if (i >= n) {
                return 0;
            }
            if (t[i][k] !== -1) {
                return t[i][k];
            }

            const not_taken = solve(i + 1, k);
            let taken = 0;
            let sum_coins = 0;

            for (let j = 0; j < Math.min(piles[i].length, k); j++) {
                sum_coins += piles[i][j];
                if (j + 1 <= k) {  // Ensure we do not exceed k
                    taken = Math.max(taken, sum_coins + solve(i + 1, k - (j + 1)));
                }
            }

            t[i][k] = Math.max(taken, not_taken);
            return t[i][k];
        };

        return solve(0, k);
};