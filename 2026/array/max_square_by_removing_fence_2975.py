class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        M = int(1e9 + 7)

        hFences.append(1)
        hFences.append(m)

        vFences.append(1)
        vFences.append(n)

        hFences.sort()
        vFences.sort()

        widths = set()
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                width = vFences[j] - vFences[i]
                widths.add(width)

        maxSide = 0
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                height = hFences[j] - hFences[i]
                if height in widths:
                    maxSide = max(maxSide, height)

        return -1 if maxSide == 0 else (maxSide * maxSide) % M
