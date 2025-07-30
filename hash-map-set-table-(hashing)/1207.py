
# Tc = O(n)
# Sc = O(n)
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr):
        freq_map = Counter(arr)
        freq_set = set()
        for freq in freq_map.values():
            if freq in freq_set:
                return False
            freq_set.add(freq)
        return True
    
class Solution:
    def uniqueOccurrences(self, arr):
        vec = [0] * 2001
        for x in arr:
            vec[x + 1000] += 1
        vec.sort()
        for i in range(1, 2001):
            if vec[i] != 0 and vec[i] == vec[i-1]:
                return False
        return True