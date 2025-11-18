class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0
        while i < n - 1:
            i += 2 if bits[i] == 1 else 1
        return i == n - 1

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        count1 = 0
        i = n - 2
        while i >= 0 and bits[i] == 1:
            count1 += 1
            i -= 1
        return count1 % 2 == 0
