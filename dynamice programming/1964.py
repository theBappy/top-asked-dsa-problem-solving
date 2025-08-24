# Meta, Twitter
# Actually LIS

# Tc = O(n* (log.m)) [outer loops run n times for the obstacles size, and log.m is for the binary search on LIS vector for upper_bound(just bigger element)]
# Sc = O(n) [due to storage of result vector and LIS vector]

from bisect import bisect_right

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles):
        # Get the number of obstacles
        n = len(obstacles)
        # This will store the longest increasing subsequence
        LIS = []
        # This will store the result for each position
        result = [0] * n

        # Iterate through each obstacle
        for i in range(n):
            # Find the index where the current obstacle can be placed
            idx = bisect_right(LIS, obstacles[i])
            # If idx is equal to the length of LIS, it means we can extend the LIS
            if idx == len(LIS):
                LIS.append(obstacles[i])  # Add the current obstacle to LIS
            else:
                LIS[idx] = obstacles[i]  # Replace the element at idx with the current obstacle
            # Store the length of the LIS at this position (idx + 1)
            result[i] = idx + 1
        
        return result
