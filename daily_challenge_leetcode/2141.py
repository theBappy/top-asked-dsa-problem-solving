class Solution:
    def possible(self, batteries: List[int], mid: int, n: int) -> bool:
        target = mid * n
        total = 0
        for b in batteries:
            total += min(b, mid)
            if total >= target:
                return True
        return False

    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        total = sum(batteries)
        l, r = 0, total // n
        ans = 0
        while l <= r:
            mid = l + (r - l) // 2
            if self.possible(batteries, mid, n):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
