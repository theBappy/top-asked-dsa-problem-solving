# Google

# Each other's moves independent
# From the very beginning, both's move is fixed
# Equal chance alice loose
# Less than 1 chance alice loose
# Only in greater than 1 chance Alice win

# Tc = O(n)

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        alice = 0
        bob = 0
        for i in range(1, n-1):
            if colors[i-1] == colors[i] and colors[i+1] == colors[i]:
                if colors[i] == 'A':
                    alice += 1
                else:
                    bob += 1
        return alice > bob
        
