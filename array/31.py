class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        pivot = -1

        # Step 1: Find the pivot
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pivot = i - 1
                break

        # Step 2: If a pivot was found
        if pivot != -1:
            # Step 3: Find the successor to swap with pivot
            successor = n - 1
            while nums[successor] <= nums[pivot]:
                successor -= 1
            # Step 4: Swap the pivot with the successor
            nums[pivot], nums[successor] = nums[successor], nums[pivot]

        # Step 5: Reverse the suffix
        nums[pivot + 1:] = reversed(nums[pivot + 1:])

# Test Example
nums = [1, 2, 3]
solution = Solution()
solution.nextPermutation(nums)
print(nums)  # Output: [1, 3, 2]
