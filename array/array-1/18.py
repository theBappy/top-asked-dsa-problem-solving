# Tc = O(n^3)
# Sc = O(1) [ignoring result storage]

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return res


# Tc = O(n^2)
# Sc = O(n^2)
# Hasp map
# But it will give TLE
from typing import List
from collections import defaultdict


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()  # helps with duplicates
        pair_sum = defaultdict(list)
        res = set()

        # Step 1: Store all pairs in hashmap
        for i in range(n):
            for j in range(i + 1, n):
                curr_sum = nums[i] + nums[j]
                complement = target - curr_sum

                # Step 2: Check if complement exists
                if complement in pair_sum:
                    for a, b in pair_sum[complement]:
                        # Ensure all indices are unique
                        if b < i:
                            quadruplet = (nums[a], nums[b], nums[i], nums[j])
                            res.add(tuple(sorted(quadruplet)))

                # Step 3: Store this pair for future
                pair_sum[curr_sum].append((i, j))

        return [list(q) for q in res]
