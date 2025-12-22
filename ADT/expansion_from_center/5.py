# Tc = O(n^2)
# Sc = O(1)

def longestPalindrome(s):
    n = len(s)

    # Edge case of string length 0 or 1
    if n <= 1:
        return s

    start = 0
    maxLength = 1

    # Helper function to expand around center
    def expandAroundCenter(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    # Iterate through each character in the string
    for i in range(n):
        len1 = expandAroundCenter(i, i)
        len2 = expandAroundCenter(i, i + 1)
        currLen = max(len1, len2)

        # Update longest
        if currLen > maxLength:
            maxLength = currLen
            start = i - (currLen - 1) // 2

    # Return result
    return s[start:start + maxLength]