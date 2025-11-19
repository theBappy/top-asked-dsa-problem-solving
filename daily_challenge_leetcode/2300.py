
from typing import List
from bisect import bisect_left
import math

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        potion_count = len(potions)
        result = []
        for spell_power in spells:
            required_strength = math.ceil(success / spell_power)
            if required_strength > potions[-1]:
                result.append(0)
                continue
            index = bisect.bisect_left(potions, required_strength)
            result.append(potion_count - index)
        return result


 
class Solution(object):
    def lowerBound(self, l, r, potions, minPotion):
        possibleIndex = -1
        while l <= r:
            mid = l + (r - l) // 2
            if potions[mid] >= minPotion:
                possibleIndex = mid
                r = mid - 1
            else:
                l = mid + 1
        return possibleIndex
    def successfulPairs(self, spells, potions, success):
        m = len(spells)
        n = len(potions)
        potions.sort()
        maxPotion = potions[-1]
        answer = []

        for i in range(m):
            spell = spells[i]
            minPotion = math.ceil(success * 1.0 / spell)
            if minPotion > maxPotion:
                answer.append(0)
                continue
            index = self.lowerBound(0, n - 1, potions, minPotion)
            answer.append(n - index)

        return answer

        