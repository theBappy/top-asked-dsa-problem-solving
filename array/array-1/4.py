class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m = len(nums1)
        n = len(nums2)
        low = 0
        high = m
        while low <= high:
            px = low + (high - low) // 2
            py = (m + n + 1) // 2 - px

            x1 = float("-inf") if px == 0 else nums1[px - 1]
            x3 = float("inf") if px == m else nums1[px]

            x2 = float("-inf") if py == 0 else nums2[py - 1]
            x4 = float("inf") if py == n else nums2[py]

            if x1 <= x4 and x2 <= x3:
                if (m + n) % 2 == 0:
                    return (max(x1, x2) + min(x4)) // 2.0
                return max(x1, x2)

            elif x1 > x4:
                hight = px - 1
            else:
                low = px + 1
        return -1.0
