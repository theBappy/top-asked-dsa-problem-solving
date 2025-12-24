
from itertools import accumulate
from operator import itemgetter


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        totalApple = sum(apple)
        count = 0
        i = 0
        while totalApple > 0:
            totalApple -= capacity[i]
            count += 1
            i += 1
        return count



from collections import Counter
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        totalApples = sum(apple)
        freq = Counter(capacity)
        count = 0
        for cap in range(50, 0, -1):
            while freq[cap] > 0 and totalApples > 0:
                totalApples -= cap
                freq[cap] -= 1
                count += 1
                if totalApples <= 0:
                    break
            if totalApples <= 0:
                break
        return count
