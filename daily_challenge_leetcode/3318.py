class Solution(object):
    def findTopXSum(self, mp, x):
        pq = []
        for val, freq in mp.items():
            heappush(pq, (freq, val))
            if len(pq) > x:
                heappop(pq)
        sum_ = 0
        while pq:
            freq, val = heappop(pq)
            sum_ += freq * val
        return sum_
    def findXSum(self, nums, k, x):
        n = len(nums)
        mp = {}
        result = []
        i = 0
        j = 0
        while j < n:
            mp[nums[j]] = mp.get(nums[j], 0) + 1
            if j - i + 1 == k:
                result.append(self.findTopXSum(mp, x))
                mp[nums[i]] -= 1
                if mp[nums[i]] == 0:
                    del mp[nums[i]]
                i += 1
            j += 1
        return result