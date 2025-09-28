# Tc = O(n^3)

from math import hypot, sqrt

class Solution(object):
    def largestTriangleArea(self, points):
        def shoelace(p1, p2, p3):
            (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
            return 0.5 * abs(x1 * (y2 - y3) +
                             x2 * (y3 - y1) +
                             x3 * (y1 - y2))

        n = len(points)
        maxArea = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    maxArea = max(maxArea, shoelace(points[i], points[j], points[k]))
        return maxArea
