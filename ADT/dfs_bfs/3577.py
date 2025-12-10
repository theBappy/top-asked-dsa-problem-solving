class Solution:
    def __init__(self):
        self.M = int(1e9 + 7)

    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        result = 1
        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0
            result = (result * i) % self.M
        return result
