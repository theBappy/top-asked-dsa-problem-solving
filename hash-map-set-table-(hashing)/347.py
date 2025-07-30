# Tc = O(n * logk)
# Sc = O(n)

from collections import defaultdict
from typing import List
class Solution:
    def topKFrequentElement(self, nums: List[int], k : int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        heap = []
        for key, val in d.items():
            if len(heap) < k or val > heap[0][0]:
                heapq.heappush(heap, [val, key])
            if len(heap) > k:
                heapq.heappop(heap)
        return [i[1] for i in heap]
        
