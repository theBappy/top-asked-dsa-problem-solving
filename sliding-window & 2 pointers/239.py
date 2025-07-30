
# Tc = O(n) for each element exactly one push and pop
# Sc = O(k)
from collections import deque
def maxSlidingWindow(nums,k):
    deq = deque()
    result = []
    for i, num in enumerate(nums):
        while deq and deq[0] <= i - k:
            deq.popleft()
        while deq and nums[deq[-1]] < num:
            deq.pop()
        deq.append(i)
        if i >= k - 1:
            result.append(nums[deq[0]])
    return result

from collections import deque

def maxSlidingWindow(nums, k):
    
    # Initialize a deque to store indices of elements in the current window
    # The deque maintains elements in decreasing order of their values
    deq = deque()
    result = []
    
    # Iterate through each element in the input array
    for i, num in enumerate(nums):
        # Remove indices from the front that are outside the current window
        # Window boundaries: [i-k+1, i]
        while deq and deq[0] <= i - k:
            deq.popleft()
        
        # Remove indices from the back whose corresponding elements are <= current element
        # This maintains the deque in decreasing order
        while deq and nums[deq[-1]] <= num:
            deq.pop()
        
        # Add current element's index to the deque
        deq.append(i)
        
        # Once window size is reached, add the maximum to the result
        # The maximum is always at the front of the deque
        if i >= k - 1:
            result.append(nums[deq[0]])

    return result




