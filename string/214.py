class Solution:
    def computeLPS(self, pattern: str) -> list:
        M = len(pattern)
        LPS = [0] * M
        length = 0  # Length of the previous longest prefix suffix
        i = 1
        while i < M:
            if pattern[i] == pattern[length]:
                length += 1
                LPS[i] = length
                i += 1
            else:
                if length != 0:
                    length = LPS[length - 1]
                else:
                    LPS[i] = 0
                    i += 1
        return LPS

    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]  # Reverse the string
        temp = s + '-' + rev  # Concatenate original and reversed string with a separator
        LPS = self.computeLPS(temp)  # Compute the LPS array
        longestLPSLength = LPS[-1]  # Length of the longest palindromic prefix
        culprit = rev[:len(s) - longestLPSLength]  # Characters to prepend
        return culprit + s  # Return the shortest palindrome

# Example usage:
sol = Solution()
print(sol.shortestPalindrome("aacecaaa"))  # Output: "aaacecaaa"



# Tc = O(n^2)
# Sc = O(n)
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]  # Reverse the string
        for i in range(len(s)):
            # Check if the prefix of s matches the suffix of rev
            if s[:len(s) - i] == rev[i:]:
                return rev[:i] + s  # Prepend the non-matching part of rev to s
        return rev + s  # If no match, return rev + s
    