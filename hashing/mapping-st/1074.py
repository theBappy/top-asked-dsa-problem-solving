from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        # Preprocessing: Compute prefix sums for each row
        for row in range(rows):
            for col in range(1, cols):
                matrix[row][col] += matrix[row][col - 1]

        result = 0
        for startCol in range(cols):
            for currCol in range(startCol, cols):
                mp = {0: 1}  # Dictionary to store cumulative sum frequencies
                sum_val = 0
                for row in range(rows):
                    # Calculate the sum for the sub-row from startCol to currCol
                    sum_val += matrix[row][currCol] - (
                        matrix[row][startCol - 1] if startCol > 0 else 0
                    )

                    # Check if (sum_val - target) exists in the map
                    if sum_val - target in mp:
                        result += mp[sum_val - target]

                    # Update the map with the current sum_val
                    mp[sum_val] = mp.get(sum_val, 0) + 1

        return result
