# Tc = O(n) go through every single character
# Sc = O(1)  

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = {'a', 'e', 'i', 'o','u', 'A', 'E', 'I', 'O','U'}
        left , right = 0, len(s)
        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -=1
            else:
                s[left], s[right] = s[right],s[left]
                left += 1
                right -= 1
        return ''.join(s)