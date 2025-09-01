# Google, Apple

# Three pointer technique
# Tc  = O(n.logn)
# Sc = O(1)

# Approach-1
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        result = 0
        piles.sort()
        bob = 0
        myself = n - 2
        while myself > bob:
            result += piles[myself]
            myself -= 2
            bob += 1
        return result
    
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        result = 0
        piles.sort()
        for M in range(n // 3, n, 2):
            result += piles[M]
        return result
    

