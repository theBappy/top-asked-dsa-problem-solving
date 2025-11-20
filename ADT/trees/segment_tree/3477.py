class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        unplaced = 0
        for i in range(n):
            placed = False
            for j in range(n):
                if fruits[i] <= baskets[j]:
                    placed = True
                    baskets[j] = -1
                    break
            if not placed:
                unplaced += 1
        return unplaced
