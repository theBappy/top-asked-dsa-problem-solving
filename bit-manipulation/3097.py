# Apple, Amazon

# Cumulative bitwise OR always non-decreasing
# Tc = O(n)
# Sc = O(32) => O(1)

class Solution:
    def update_window(self, num, vec, val):
        for i in range(32):  # O(32) => O(1)
            if (num >> i) & 1:
                vec[i] += val

    def get_decimal_from_binary(self, vec):
        num = 0
        for i in range(32):  # O(32) => O(1)
            if vec[i] > 0:  # i'th position 1?
                num |= (1 << i)
        return num

    def minimum_subarray_length(self, nums, k):
        n = len(nums)
        result = float('inf')
        i = 0
        j = 0
        vec = [0] * 32  # vec[i] = total number of set bits in i'th position

        # Tc = O(2* n) [twice visiting each element]
        while j < n:  # O(n)
            # Tc = O(2* n) [twice visiting each element]
            self.update_window(nums[j], vec, 1)  # adding in current window
            while i <= j and self.get_decimal_from_binary(vec) >= k:
                result = min(result, j - i + 1)
                self.update_window(nums[i], vec, -1)  # remove nums[i] from window
                i += 1
            j += 1

        return result if result != float('inf') else -1


