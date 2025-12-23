/**
 * @param {number[][]} events
 * @return {number}
 */
var maxTwoEvents = function(events) {

    const n = events.length;

    // Sort events by start time
    events.sort((a, b) => a[0] - b[0]);

    // DP table: dp[i][count]
    // i = event index
    // count = how many events taken (0 or 1)
    const dp = Array.from({ length: n }, () => Array(2).fill(-1));

    /**
     * Binary search to find the first event
     * whose start time is > given endTime
     */
    function binarySearch(endTime) {
        let left = 0;
        let right = n - 1;
        let result = n;

        while (left <= right) {
            const mid = Math.floor((left + right) / 2);
            if (events[mid][0] > endTime) {
                result = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return result;
    }

    /**
     * Recursive DP function
     * @param {number} i - current index
     * @param {number} count - events taken so far
     */
    function solve(i, count) {

        // Base case: taken 2 events or no events left
        if (count === 2 || i >= n) return 0;

        // Memoized result
        if (dp[i][count] !== -1) {
            return dp[i][count];
        }

        // Option 1: take the current event
        const nextIndex = binarySearch(events[i][1]);
        const take = events[i][2] + solve(nextIndex, count + 1);

        // Option 2: skip the current event
        const skip = solve(i + 1, count);

        // Store and return best option
        dp[i][count] = Math.max(take, skip);
        return dp[i][count];
    }

    // Start from index 0 with 0 events taken
    return solve(0, 0);
};
