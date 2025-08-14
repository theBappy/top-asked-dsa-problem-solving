class Solution {
    constructor() {
        // Initialize memoization table (301 jobs max, 11 days max)
        // Filled with -1 to indicate un-computed states
        this.t = Array.from({length: 301}, () => Array(11).fill(-1));
    }

    solve(jd, n, idx, d) {
        // Base case: Only 1 day left - must do all remaining jobs
        // Find maximum difficulty in remaining jobs
        if (d === 1) {
            let maxD = -Infinity;
            for (let i = idx; i < n; i++) {
                maxD = Math.max(maxD, jd[i]);
            }
            return maxD;
        }

        // Return memoized result if already computed
        if (this.t[idx][d] !== -1) {
            return this.t[idx][d];
        }

        let maxD = -Infinity;  // Tracks max difficulty for current day's jobs
        let finalResult = Infinity;  // Tracks minimum total difficulty found

        // Try all possible partitions of jobs for current day
        for (let i = idx; i <= n - d; i++) {
            maxD = Math.max(maxD, jd[i]);  // Update day's max difficulty
            // Recursively solve for remaining days and jobs
            const result = maxD + this.solve(jd, n, i + 1, d - 1);
            // Keep track of minimum difficulty schedule found
            finalResult = Math.min(finalResult, result);
        }

        // Memoize result before returning
        this.t[idx][d] = finalResult;
        return finalResult;
    }

    minDifficulty(jd, d) {
        const n = jd.length;
        // Edge case: Not enough jobs for each day to have at least one
        if (n < d) {
            return -1;
        }
        // Start solving from first job (index 0) with all days remaining
        return this.solve(jd, n, 0, d);
    }
}

// Example usage:
// const sol = new Solution();
// console.log(sol.minDifficulty([6,5,4,3,2,1], 2)); // Output: 9
// console.log(sol.minDifficulty([9,9,9], 4)); // Output: -1
