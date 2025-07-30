# Tc = O(n)
# Sc = O(n)
from collections import defaultdict
import math
class Solution:
    def numRabbits(self, answers):
        mp = defaultdict(int)
        for x in answers:
            mp[x] += 1     
        total = 0
        for x, count in mp.items():
            group_size = x + 1
            groups = math.ceil(count / group_size)
            total += groups * group_size 
        return total