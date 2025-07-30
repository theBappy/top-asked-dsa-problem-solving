class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left , right = i + 1, j - 1
            return True
        left,right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return check(left + 1, right) or check(left, right-1)
            i, j = i + 1, j- 1
        return True
# Tc = O(n)
# Sc = O(1)