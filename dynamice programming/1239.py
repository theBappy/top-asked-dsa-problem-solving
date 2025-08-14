# Microsoft, Apple
# only concatenate when two string doesn't have any common char or element
# Recursion + Memoization
# Tc = O(n * 2^n)
# Sc = O(n)

class Solution:
    def hasDuplicate(self, s1, s2):
        arr = [0] * 26
        for ch in s1:
            if arr[ord(ch) - ord('a')] > 0:
                return True
            arr[ord(ch) - ord('a')] += 1
        for ch in s2:
            if arr[ord(ch) - ord('a')] > 0:
                return True
        return False  # no duplicate found at all

    def solve(self, i, arr, temp, n, memo):
        if i >= n:
            return len(temp)
        if temp in memo:
            return memo[temp]

        include = 0
        exclude = 0

        if self.hasDuplicate(arr[i], temp):  # exclude only
            exclude = self.solve(i + 1, arr, temp, n, memo)
        else:  # include and exclude
            exclude = self.solve(i + 1, arr, temp, n, memo)
            include = self.solve(i + 1, arr, temp + arr[i], n, memo)

        memo[temp] = max(include, exclude)
        return memo[temp]

    def maxLength(self, arr):
        memo = {}
        n = len(arr)
        return self.solve(0, arr, "", n, memo)
