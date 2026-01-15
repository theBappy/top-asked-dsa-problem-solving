class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        hBars.sort()
        vBars.sort()

        maxConsecutiveHBars = 1
        maxConsecutiveVBars = 1

        currConsecutiveHBars = 1
        for i in range(1, len(hBars)):
            if hBars[i] - hBars[i - 1] == 1:
                currConsecutiveHBars += 1
            else:
                currConsecutiveHBars = 1
            maxConsecutiveHBars = max(maxConsecutiveHBars, currConsecutiveHBars)

        currConsecutiveVBars = 1
        for i in range(1, len(vBars)):
            if vBars[i] - vBars[i - 1] == 1:
                currConsecutiveVBars += 1
            else:
                currConsecutiveVBars = 1
            maxConsecutiveVBars = max(maxConsecutiveVBars, currConsecutiveVBars)

        side = min(maxConsecutiveHBars, maxConsecutiveVBars) + 1
        return side * side
