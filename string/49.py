# Tc = O(n.k)
# Sc = O(n.k)
from typing import List
from collections import defaultdict
class Solution:
    def getSignature(self, s:str) ->str:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        result = []
        for i in range(26):
            if count[i] != 0:
                result.extend([chr(i+ord('a')), str(count[str])])
        return ''.join(result)
    def  groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        groups = defaultdict(list)
        for s in strs:
            groups[self.getSignature(s)].append(s)
        result.extend(groups.values())
        return result
    

# Tc = O(n*klogk) [k = maximum size of string in the input and n = size of input]
# Sc = O(n.k)
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        n = len(strs)
        result = []
        mp = defaultdict(list)
        for i in range(n):
            temp = ''.join(sorted(strs[i]))
            mp[temp].append(strs[i])
        for it in mp.values():
            result.append(it)
        return result
    

