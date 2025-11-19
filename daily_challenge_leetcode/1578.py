class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        time = 0
        prevMax = 0
        for i in range(n):
            if i > 0 and colors[i] != colors[i - 1]:
                prevMax = 0
            curr = neededTime[i]
            time += min(prevMax, curr)
            prevMax = max(prevMax, curr)
        return time
