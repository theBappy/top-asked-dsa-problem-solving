



# Tc = O(n + m)
# Sc = O(m) : m is the number of unique characters
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        if len(t) > s:
            return ""
        mp = defaultdict(int)
        for ch in t:
            mp[ch] += 1
        requiredCount = len(t)
        i = 0
        j = 0
        minWindowSize = float('inf')
        start_i = 0
        while j < n:
            ch = s[j]
            if mp[ch] > 0:
                requiredCount -= 1
            mp[ch] -= 1
            while requiredCount == 0:
                currWindowSize = j - i + 1
                if minWindowSize > currWindowSize:
                    minWindowSize = currWindowSize
                    start_i = i
                mp[s[i]] += 1
                if mp[s[i]] > 0:
                    requiredCount += 1
                i += 1
            j += 1
        return "" if minWindowSize == float('inf') else s[start_i:start_i + minWindowSize]
    


from collections import defaultdict
class Solution:
    def minWindow(self, s:str, t:str) -> str:
        n = len(s)
        if len(t) > n:
            return ''
        mp = defaultdict(int)
        for ch in t:
            mp[ch] += 1

        requiredCount = len(t)
        i = 0
        j = 0
        minWindowSize = float('inf')
        start_i = i
        while j < n:
            ch = s[j]
            if mp[ch] > 0:
                requiredCount -= 1
            mp[ch] -= 1
            while requiredCount == 0:
                currWindowSize = j - i +1
                if minWindowSize > currWindowSize:
                    minWindowSize = currWindowSize
                    start_i = i
                mp[s[i]] += 1
                if mp[s[i]] > 0:
                    requiredCount += 1
                i += 1
            j += 1
        return "" if minWindowSize == float('inf') else s[start_i:start_i + minWindoSize]
