class Solution:
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        n = len(bottomLeft)

        maxSide = 0

        for i in range(n):
            for j in range(i + 1, n):
                topRightX = min(topRight[i][0], topRight[j][0])
                bottomLeftX = max(bottomLeft[i][0], bottomLeft[j][0])
                width = topRightX - bottomLeftX

                topRightY = min(topRight[i][1], topRight[j][1])
                bottomLeftY = max(bottomLeft[i][1], bottomLeft[j][1])
                height = topRightY - bottomLeftY

                side = min(width, height)
                maxSide = max(maxSide, side)
        return maxSide * maxSide
