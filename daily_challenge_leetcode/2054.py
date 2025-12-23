class Solution:
    def __init__(self):
        self.n = 0
        self.t = []

    def binarySearch(self, events: List[List[int]], endTime: int) -> int:
        l, r = 0, self.n - 1
        result = self.n
        while l <= r:
            mid = l + (r - l) // 2
            if events[mid][0] > endTime:
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        return result

    def solve(self, events: List[List[int]], i: int, count: int) -> int:
        if count == 2 or i >= self.n:
            return 0
        if self.t[i][count] != -1:
            return self.t[i][count]
        nextValidIndex = self.binarySearch(events, events[i][1])
        take = events[i][2] + self.solve(events, nextValidIndex, count + 1)
        skip = self.solve(events, i + 1, count)
        self.t[i][count] = max(take, skip)
        return self.t[i][count]

    def maxTwoEvents(self, events: List[List[int]]) -> int:
        self.n = len(events)
        events.sort()
        self.t = [[-1] * 3 for _ in range(self.n)]
        count = 0
        return self.solve(events, 0, count)