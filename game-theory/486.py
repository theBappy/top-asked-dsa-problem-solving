# Amazon

# Optimal game strategy(min-max game strategy)
# When your turn do your best(max), and when opponent's turn expect the worst(min)

# Approach-1
# Tc = O(2^n) but with memoization Tc = O(n^2) [computed only once] [can choose between 2 options]
# Sc = O(n^2) [memoization table]
class Solution(object):
    def __init__(self):
        self.t = [[-1] * 23 for _ in range(23)]

    def solve(self, i, j, nums):
        if i > j:
            return 0
        if i == j:
            return nums[i]
        if self.t[i][j] != -1:
            return self.t[i][j]
        
        take_i = nums[i] + min(self.solve(i + 2, j, nums), self.solve(i + 1, j - 1, nums))
        take_j = nums[j] + min(self.solve(i + 1, j - 1, nums), self.solve(i, j - 2, nums))
        self.t[i][j] = max(take_i, take_j)
        return self.t[i][j]

    def predictTheWinner(self, nums):
        self.t = [[-1] * 23 for _ in range(23)]
        total_score = sum(nums)
        p1_score = self.solve(0, len(nums) - 1, nums)
        p2_score = total_score - p1_score
        return p1_score >= p2_score
    
