# Tc = O(n + k) [n is the number of elements and k that checks the pairs remainders]
# Sc = O(k) [for mp list which counts for each possible remainder]
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mp = [0] * k
        for num in arr:
            remainder = num % k
            if remainder < 0:
                remainder += k  # handling negative remainders
            mp[remainder] += 1
        
        if mp[0] % 2 != 0:
            return False
        
        for remainder in range(1, (k // 2) + 1):
            counterHalf = k - remainder
            if mp[counterHalf] != mp[remainder]:
                return False
        
        return True
