/**
 * Weighted Job Scheduling Problem
 * Given start times, end times, and profits for jobs,
 * choose non-overlapping jobs to maximize profit.
 * 
 * Time Complexity: O(n log n)
 * Space Complexity: O(n)
 */
var jobScheduling = function (startTime, endTime, profit) {
    const n = startTime.length;

    // Combine jobs into an array of objects for clarity
    const jobs = [];
    for (let i = 0; i < n; i++) {
        jobs.push({ start: startTime[i], end: endTime[i], profit: profit[i] });
    }

    // Sort jobs by start time
    jobs.sort((a, b) => a.start - b.start);

    // Extract start times separately for binary search
    const starts = jobs.map(job => job.start);

    // Memoization array: -1 means "not calculated yet"
    const memo = new Array(n).fill(-1);

    /**
     * Binary search: find the first job whose start >= currentEnd
     * @param {number} currentEnd - End time of the current job
     * @returns {number} Index of the next job or n if none found
     */
    function getNextIndex(currentEnd) {
        let left = 0, right = n - 1;
        let result = n; // n means "no next job found"

        while (left <= right) {
            const mid = Math.floor((left + right) / 2);
            if (starts[mid] >= currentEnd) {
                result = mid;
                right = mid - 1; // Search left half for earlier job
            } else {
                left = mid + 1; // Search right half
            }
        }
        return result;
    }

    /**
     * Recursive DP function to compute max profit starting from job index i
     * @param {number} i - Current job index
     * @returns {number} Maximum profit achievable from job i onward
     */
    function solve(i) {
        if (i >= n) return 0; // No jobs left

        if (memo[i] !== -1) return memo[i]; // Return cached result

        // Option 1: Take this job
        const nextIndex = getNextIndex(jobs[i].end);
        const takeProfit = jobs[i].profit + solve(nextIndex);

        // Option 2: Skip this job
        const skipProfit = solve(i + 1);

        // Store the best choice
        memo[i] = Math.max(takeProfit, skipProfit);
        return memo[i];
    }

    // Start solving from the first job
    return solve(0);
};


