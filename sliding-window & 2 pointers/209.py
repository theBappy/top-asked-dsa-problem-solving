# Tc =O(n)
# Sc = O(1)

def minSubArrayLen(target: int, nums: List[int]) -> int:
    left = 0
    current_sum = 0
    min_length = float('inf')
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0

# Example usage:
print(minSubArrayLen(7, [2,3,1,2,4,3]))  # Output: 2 (subarray [4,3])

