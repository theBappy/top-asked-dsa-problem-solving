from typing import List
import sys

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure binary search on the smaller array for better performance
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            # Partition index in nums1
            px = (low + high) // 2
            # Partition index in nums2 such that left half has half the total elements
            py = (m + n + 1) // 2 - px

            # Get values around the partition in nums1
            x1 = float('-inf') if px == 0 else nums1[px - 1]  # left of partition
            x3 = float('inf') if px == m else nums1[px]       # right of partition

            # Get values around the partition in nums2
            x2 = float('-inf') if py == 0 else nums2[py - 1]  # left of partition
            x4 = float('inf') if py == n else nums2[py]       # right of partition

            # Check if we have a correct partition
            if x1 <= x4 and x2 <= x3:
                # Total length is odd: max of left half
                if (m + n) % 2 == 1:
                    return max(x1, x2)
                # Total length is even: average of two middle values
                return (max(x1, x2) + min(x3, x4)) / 2.0
            elif x1 > x4:
                # Move search range left
                high = px - 1
            else:
                # Move search range right
                low = px + 1

        # This line should never be reached if input is valid
        return -1
