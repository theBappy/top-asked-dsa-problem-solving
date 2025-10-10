# Using Sorting
# T.C : O(n*klog(k))  (n = size of input, k = maximum length of a string in the input vector)
# S.C : O(n*k)

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        mp = defaultdict(list)
        for s in strs:
            temp = ''.join(sorted(s))
            mp[temp].append(s)
        return list(mp.values())
    
# without sorting
class Solution:
    def generate(self, s: str) -> str:
        count = [0] * 26
        
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        
        new_s = []
        for i in range(26):
            if count[i] > 0:
                new_s.append(chr(i + ord('a')) * count[i])
        
        return ''.join(new_s)
    
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mp = defaultdict(list)
        
        for s in strs:
            new_s = self.generate(s)
            mp[new_s].append(s)
        
        return list(mp.values())