from collections import deque

def sliding_window_maximum(nums, k):
    """
    Finds the maximum element for each sliding window of size k.
    
    Args:
        nums: A list of integers.
        k: The size of the sliding window.
        
    Returns:
        A list of maximums for each window.
    """
    result = []
    dq = deque()  # Stores indices of elements
    
    for i in range(len(nums)):
        # Remove indices that are out of the current window
        if dq and dq[0] == i - k:
            dq.popleft()
            
        # Remove indices of elements smaller than the current one from the back
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
            
        # Add the current index to the deque
        dq.append(i)
        
        # Add the maximum for the first full window and all subsequent ones
        if i >= k - 1:
            result.append(nums[dq[0]])
            
    return result

# Example usage
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_maximum(nums, k))