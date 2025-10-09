from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        return next((s for s in words if s==s[::-1]), "")
    
    
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        ans = ""
        for i in words:
            if i==i[::-1]:
                ans += i
                break
        return ans