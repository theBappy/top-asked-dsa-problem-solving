# Tc = O(n* klogk)
# Sc = O(n)

from collections import Counter
class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
    
        n = len(hand)
        if n % groupSize != 0:
            return False
        count = Counter(hand)
        for curr in sorted(count):
            while count[curr]:
                for i in range(groupSize):
                    if count[curr+i] == 0:
                        return False
                    count[curr+i] -= 1
                    if count[curr+i] == 0:
                        del count[curr+i]
        return True