class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        total_sum = 0
        count_negatives = 0
        smallest_abs_value = float("inf")
        for i in range(n):
            for j in range(n):
                val = matrix[i][j]
                total_sum += abs(val)
                if val < 0:
                    count_negatives += 1
                smallest_abs_value = min(smallest_abs_value, abs(val))

        if count_negatives % 2 == 0:
            return total_sum
        
        return total_sum - 2 * smallest_abs_value
