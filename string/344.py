# Tc =O(n) loop through all the elements
# Sc = O(1) in place swap
class Solution: 
    def reverseString(self, s:list[str]) -> None:
        l, r = 0, n-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1

# Tc =O(n) loop through all the elements
# Sc = O(n) for stack
class Solution: 
    def reverseString(self, s:list[str]) -> None:
        stack = []
        for c in s:
            stack.append(c)
        i = 0
        while stack:
            s[i] = stack.pop()
            i += 1



# Tc =O(n) loop through all the elements
# Sc = O(n) recursion takes extra space
class Solution: 
    def reverseString(self, s:list[str]) -> None:
        def reverse(l, r):
            if l < r:
                s[l], s[r] = s[l], s[r]
                reverse(l+1, r-1)
        reverse(0, len(s) -1)
                
        

