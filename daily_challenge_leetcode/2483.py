class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        minHour = 0
        penalty = customers.count("Y")
        minPenalty = penalty
        for i in range(n):
            if customers[i] == "Y":
                penalty -= 1
            else:
                penalty += 1
            if penalty < minPenalty:
                minHour = i + 1
                minPenalty = penalty
        return minHour
