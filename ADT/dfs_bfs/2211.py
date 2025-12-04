
# Tc = O(n)
# Sc = O(1)
class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        i = 0
        while i < n and directions[i] == "L":
            i += 1
        j = n - 1
        while j >= 0 and directions[j] == "R":
            j -= 1
        collisions = 0
        while i <= j:
            if directions[i] != "S":
                collisions += 1
            i += 1
        return collisions
