
# Expansion from center
# Tc = O(n^2)
#  Sc = O(1)
'''

#### The idea is to traverse each character in the string and treat it as a potential center of a palindrome, trying to expand around it in both directions while checking if the expanded substring remains a palindrome. 

For each position, we check for both odd-length palindromes (where the current character is the center) and even-length palindromes (where the current character and the next character together form the center).
 As we expand outward from each center, we keep track of the start position and length of the longest palindrome found so far, updating these values whenever we find a longer valid palindrome.
#### Step-by-step approach:

#### Use two pointers, low and hi, for the left and right end of the current palindromic substring being found. 
Then checks if the characters at s[low] and s[hi] are the same. 
If they are, it expands the substring to the left and right by decrementing low and incrementing hi. 
It continues this process until the characters at s[low] and s[hi] are unequal or until the indices are in bounds.
If the length of the current palindromic substring becomes greater than the maximum length, it updates the maximum length.

'''


def longestPalindrome(s):
    n = len(s)
    if n == 0:
        return ''
    start, maxLen = 0, 1
    for i in range(n):
        for j in range(2):
            low, high = i , i + j
            while low >= 0 and high < n and s[low] == s[high]:
                currLen = high - low + 1
                if currLen > maxLen:
                    start = low
                    maxLen = currLen
                low -= 1
                high += 1
    return s[start:start+maxLen]


# def longestPalindrome(s):
#     n = len(s)
#     if n == 0:
#         return ''
#     start, maxLen = 0, 1
#     for i in range(n):
#         for j in range(2):
#             low, high = i, i + j
#             while low >= 0 and high < n  and s[low] == s[high]:
#                 currLen = high - low + 1
#                 if currLen > maxLen:
#                     maxLen = currLen
#                     start = low
#                 low -= 1
#                 high += 1
#     return s[start:start+maxLen]

# def longestPalindrome(s):
#     n = len(s)
#     if n == 0:
#         return ''
#     start, maxLen = 0, 1
#     for i in range(n):
#         for j in range(2):
#             low , high = i , i + j
#             while low >= 0 and high < n and s[low] == s[high]:
#                 currLen = high - low + 1
#                 if currLen > maxLen:
#                     start = low
#                     maxLen = currLen
#                 low -= 1
#                 high += 1
#     return s[start:start+maxLen]
