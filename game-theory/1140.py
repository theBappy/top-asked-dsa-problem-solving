# Meta

# When your turn do your best(max), when opponent's turn expect worst(min)
# Tc = O(n^3)
# Sc = O(n^3)

class Solution:
    
    def stoneGameII(self, piles):
        self.n = len(piles)
        self.t = [[[-1] * (self.n + 1) for _ in range(self.n + 1)] for _ in range(2)]
        return self.solveForAlice(piles, 1, 0, 1)

    def solveForAlice(self, piles, person, i, M):
        if i >= self.n:
            return 0
        
        if self.t[person][i][M] != -1:
            return self.t[person][i][M]
        
        result = float('-inf') if person == 1 else float('inf')
        stones = 0
        
        for x in range(1, min(2 * M, self.n - i) + 1):
            stones += piles[i + x - 1]
            
            if person == 1:  # Alice
                result = max(result, stones + self.solveForAlice(piles, 0, i + x, max(M, x)))
            else:  # Bob
                result = min(result, self.solveForAlice(piles, 1, i + x, max(M, x)))
        
        self.t[person][i][M] = result
        return result



        
