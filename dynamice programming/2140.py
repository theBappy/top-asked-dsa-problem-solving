# Google
# Tc = O(n)
# Sc = O(n)

# Recur + Memo
class Solution:
    def solve(self, i, questions, t):
        if i >= self.n:
            return 0
        if t[i] != -1:
            return t[i]
        taken = questions[i][0] + self.solve(i + (questions[i][1] + 1), questions, t)
        not_taken = self.solve(i + 1, questions, t)
        t[i] = max(taken, not_taken)
        return t[i] 
    def mostPoints(self, questions):
        self.n = len(questions)
        t = [-1] * self.n
        return self.solve(0, questions, t)
