# Google, Apple

# Tc = O(n) [though two choice which is exponential but using memoization significantly reduces the number of unique states, and each state is computed only once]

# Sc = O(n) [(n+1)*2 which requires O(n) space and max depth of recursion stack is also O(n)]
# Top-down(recursion+memoization)
class Solution:
    def __init__(self):
        self.n = 0
        self.memo = []

    def solve(self, s, curr_index, prev_val):
        if curr_index >= self.n:
            return 0
        if self.memo[curr_index][prev_val] != -1:
            return self.memo[curr_index][prev_val]

        flip = float('inf')
        no_flip = float('inf')

        if s[curr_index] == '0':
            if prev_val == 1:
                flip = 1 + self.solve(s, curr_index + 1, 1)
            else:
                flip = 1 + self.solve(s, curr_index + 1, 1)
                no_flip = self.solve(s, curr_index + 1, 0)
        elif s[curr_index] == '1':
            if prev_val == 1:
                no_flip = self.solve(s, curr_index + 1, 1)
            else:
                flip = 1 + self.solve(s, curr_index + 1, 0)
                no_flip = self.solve(s, curr_index + 1, 1)

        self.memo[curr_index][prev_val] = min(flip, no_flip)
        return self.memo[curr_index][prev_val]

    def minFlipsMonoIncr(self, s: str) -> int:
        self.n = len(s)
        self.memo = [[-1 for _ in range(2)] for _ in range(self.n + 1)]
        return self.solve(s, 0, 0)  # Start with prev_val as 0

# Approach-2
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        count_of_ones = 0
        flips = 0
        for ch in s:
            if ch == '1':
                count_of_ones += 1
            else:
                flips = min(count_of_ones, flips+1)
        return flips
