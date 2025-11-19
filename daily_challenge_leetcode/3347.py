from collections import defaultdict
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        maxVal = max(nums) + k
        diff = defaultdict(int)
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

            l = max(num - k, 0)
            r = min(num + k, maxVal)

            diff[l] += 1
            diff[r + 1] -= 1

            diff[num] += 0

        result = 1
        cumSum = 0

        for target in sorted(diff.keys()):
            diff[target] += cumSum

            targetFreq = freq[target]
            needConversion = diff[target] - targetFreq

            maxPossibleFreq = min(needConversion, numOperations)

            result = max(result, targetFreq + maxPossibleFreq)

            cumSum = diff[target]

        return result
