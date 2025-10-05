
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        left , right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                    left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water




def trap(height):
    # Initialize two pointers
    left, right = 0, len(height) - 1

    # Track the maximum height from both sides
    left_max = 0
    right_max = 0

    # Variable to accumulate trapped water
    water = 0

    # Run until the two pointers meet
    while left < right:

        # Always process the side with the smaller height
        if height[left] < height[right]:
            # If current bar is higher or equal to left_max, update left_max
            if height[left] >= left_max:
                left_max = height[left]
                # No water trapped here since we just updated the boundary
            else:
                # Water trapped = left_max - current height
                trapped = left_max - height[left]
                water += trapped
                print(f"At index {left}: trapped {trapped} unit(s) of water")

            # Move the left pointer to the right
            left += 1

        else:
            # If current bar is higher or equal to right_max, update right_max
            if height[right] >= right_max:
                right_max = height[right]
                # No water trapped here since we just updated the boundary
            else:
                # Water trapped = right_max - current height
                trapped = right_max - height[right]
                water += trapped
                print(f"At index {right}: trapped {trapped} unit(s) of water")

            # Move the right pointer to the left
            right -= 1

    print(f"Total trapped water: {water}")
    return water


# -------------------------------
# 🔍 Example Dry Run
# -------------------------------
height = [0,1,0,2,1,0,1,3,2,1,2,1]
trap(height)

        