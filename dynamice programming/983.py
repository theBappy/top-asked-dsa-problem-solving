# Google
# Approach-1 (Recursion+Memoization)
# Tc = O(n) [n is the number of travel days]
# Sc = O(n)

class Solution:
    def mincostTickets(self, days, costs):
        n = len(days)
        t = [-1] * 366  # Memoization array

        def solve(i):
            if i >= n:
                return 0  # No more travel days
            if t[i] != -1:
                return t[i]

            # 1-day pass
            cost_1 = costs[0] + solve(i + 1)

            # 7-day pass
            j = i
            max_day = days[i] + 7
            while j < n and days[j] < max_day:
                j += 1
            cost_7 = costs[1] + solve(j)

            # 30-day pass
            j = i
            max_day = days[i] + 30
            while j < n and days[j] < max_day:
                j += 1
            cost_30 = costs[2] + solve(j)

            # Store the minimum cost in the memoization array
            t[i] = min(cost_1, cost_7, cost_30)
            return t[i]

        return solve(0)

# Example usage:
# solution = Solution()
# print(solution.mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))  # Output: minimum cost



# Bottom Up
# State define: t[i] = min cost to travel till day i
# need to return t[20]
# t[0] = 0 [no costs]
from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        st = set(days)
        last_day = days[-1]
        t = [0] * (last_day + 1)
        # t[i] = min cost travel till day i of your travel plan
        t[0] = 0
        # need to return last day of travel cost -> t[last_day]
        for i in range(1, last_day + 1):
            # check if have to travel day i or not
            if i not in st:
                t[i] = t[i - 1]
                continue
            t[i] = float('inf')
            d_1 = costs[0] + t[max(i - 1, 0)]
            d_7 = costs[1] + t[max(i - 7, 0)]
            d_30 = costs[2] + t[max(i - 30, 0)]
            t[i] = min(d_1, d_7, d_30)
        return t[last_day]
