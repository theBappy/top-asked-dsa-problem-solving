# Tc = O(maxEl)
# Sc = O(maxEl)


from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        maxEl = max(nums) + k
        freq = [0] * (maxEl + 1)
        for num in nums:
            freq[num] += 1
        
        # cumulative sum of freq
        for i in range(1, maxEl + 1):
            freq[i] += freq[i - 1]
        
        result = 0
        for target in range(maxEl + 1):
            if freq[target] == 0:
                continue
            leftNum = max(0, target - k)
            rightNum = min(maxEl, target + k)

            totalCount = freq[rightNum] - (freq[leftNum - 1] if leftNum > 0 else 0)
            targetCount = freq[target] - (freq[target - 1] if target > 0 else 0)

            needConversion = totalCount - targetCount
            maxPossibleFreq = targetCount + min(needConversion, numOperations)
            result = max(result, maxPossibleFreq)
        
        return result