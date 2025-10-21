from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        n = len(nums)
        mp = Counter(nums)
        bucket = [[] for _ in range(n + 1)]

        for element, freq in mp.items():
            bucket[freq].append(element)

        result = []
        for i in range(n, 0, -1):
            if not bucket[i]:
                continue
            while bucket[i] and k > 0:
                result.append(bucket[i].pop())
                k -= 1
        return result