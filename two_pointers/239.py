

# Tc = O(n) [only visiting twice each element, only push and pop]

from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        deq = deque()     # will store indexes (not values)
        result = []
        
        for i in range(n):
            while deq and deq[0] <= i - k:
                deq.popleft()  # remove elements out of this window
                
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()  # remove smaller numbers as they can't be max
                
            deq.append(i)  # add current index
            
            if i >= k - 1:
                result.append(nums[deq[0]])  # first index in deque is max
        
        return result


            