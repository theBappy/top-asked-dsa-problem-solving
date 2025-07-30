def trap(height):
    """
    Compute how much water can be trapped between the bars after raining.
    
    Args:
    height (List[int]): Array representing the elevation map
    
    Returns:
    int: Total amount of trapped water
    """
    
    # Edge case: if array is empty, no water can be trapped
    if not height:
        return 0
    
    n = len(height)
    total_water = 0
    
    # Arrays to store maximum heights to the left and right of each position
    left_max = [0] * n
    right_max = [0] * n
    
    # Initialize first element of left_max
    left_max[0] = height[0]
    
    # Fill left_max array:
    # For each position, the highest bar to the left is either:
    # 1. The previous left_max value OR
    # 2. The current height, whichever is higher
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])
    
    # Initialize last element of right_max
    right_max[n-1] = height[n-1]
    
    # Fill right_max array:
    # For each position, the highest bar to the right is either:
    # 1. The next right_max value OR
    # 2. The current height, whichever is higher
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])
    
    # Calculate trapped water for each position:
    # Water trapped at any position is equal to:
    # min(left_max[i], right_max[i]) - height[i]
    # (We only consider the smaller of the two max heights)
    for i in range(n):
        water_at_position = min(left_max[i], right_max[i]) - height[i]
        total_water += max(water_at_position, 0)  # Ensure we don't add negative values
    
    return total_water


# Example Usage:
if __name__ == "__main__":
    elevation_map = [0,1,0,2,1,0,1,3,2,1,2,1]
    print("Total trapped water:", trap(elevation_map))
    # Output should be 6

# Tc = O(n) + O(n) + O(n) overall O(n)
# Sc = O(n) + O(n) for  two different array overall O(n)

def trappingRainWater(height):
    if not height: return 0
    n = len(height)
    left_max = [0] * n
    right_max =[0] * n
    left_max[0] = height[0]
    right_max[n-1] = height[n-1]
    total_water = 0
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])
    for i in range(n):
        water_at_position = min(left_max[i], right_max[i]) - height[i]
        total_water += max(water_at_position, 0)
    return total_water
