# Google, Meta, Amazon, Abode
# To pointer
# Tc = O(n)
# Sc = O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n-1
        maxArea = 0
        while i < j:
            h = min(height[i], height[j])
            w = j - i
            area = w * h
            maxArea = max(maxArea, area)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return maxArea