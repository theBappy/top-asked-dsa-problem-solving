# Google, Amazon, Microsoft
# Changing index point
# Recursion + Memoization
# converting to integer, num = (num*10) + (s[end-'0')[not to make substring, to avoid O(n) of substring]

# Tc = O(n^2) [recursive call + inner loop each starting index which form the number, and here use of memoization optimize the performance in practical scenarios]

# Sc = O(n) [due to the memoization vector t, and recursion stack can also go up to O(n) in worst case]
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        mod = 10**9 + 7
        t = [-1] * n
        
        def solve(start: int) -> int:
            if start >= n:
                return 1
            if t[start] != -1:
                return t[start]
            if s[start] == '0':
                return 0  # no leading zero
            
            ans = 0
            num = 0
            for end in range(start, n):
                num = num * 10 + int(s[end])
                if num > k:
                    break
                ans = (ans + solve(end + 1)) % mod
            
            t[start] = ans
            return ans
        
        return solve(0)

# Example usage:
# solution = Solution()
# print(solution.numberOfArrays("1234", 100))  # Example call
