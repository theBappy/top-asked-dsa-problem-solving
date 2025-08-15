# Google, Microsoft
# Optimal/Max/Min -> DP
# Option(take, not_take) -> classic DP
# Tc = O(n*log(n))
# Sc = O(n)


from bisect import bisect_left

class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        """
        Weighted Job Scheduling Problem
        Given start times, end times, and profits for jobs,
        choose non-overlapping jobs to maximize profit.
        """

        n = len(startTime)

        # Combine jobs into a single list: [start, end, profit]
        jobs = list(zip(startTime, endTime, profit))

        # Sort jobs by start time (important for binary search)
        jobs.sort(key=lambda x: x[0])

        # Extract sorted start times separately for binary search
        starts = [job[0] for job in jobs]

        # Memoization array to store computed results for each index
        memo = [-1] * n

        def getNextIndex(current_end):
            """
            Finds the first job index whose start time >= current job's end time.
            Uses binary search for efficiency.
            """
            idx = bisect_left(starts, current_end)
            return idx  # returns n if no such job exists

        def solve(i):
            """
            Recursively decide:
            - Take the current job and jump to the next non-overlapping job.
            - Skip the current job and move to the next one.
            """
            if i >= n:
                return 0  # No more jobs left

            if memo[i] != -1:
                return memo[i]  # Return cached result

            # Option 1: Take this job
            next_index = getNextIndex(jobs[i][1])
            take_profit = jobs[i][2] + solve(next_index)

            # Option 2: Skip this job
            skip_profit = solve(i + 1)

            # Store and return the best option
            memo[i] = max(take_profit, skip_profit)
            return memo[i]

        # Start recursion from the first job
        return solve(0)


# Example usage:
if __name__ == "__main__":
    start = [1, 2, 3, 4, 6]
    end = [3, 5, 10, 6, 9]
    profit = [20, 20, 100, 70, 60]

    sol = Solution()
    print(sol.jobScheduling(start, end, profit))  # Output: 150






