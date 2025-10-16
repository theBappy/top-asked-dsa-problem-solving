class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        s1 = ''.join(sorted(s1))
        # T.C : O((m-n)*logn)
        # S.C : O(1)
        for i in range(m - n + 1):
            substring = ''.join(sorted(s2[i:i+n]))
            if s1 == substring:
                return True
        return False
    

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False
        
        s1_freq = Counter(s1)
        s2_freq = Counter()
        
        i = 0
        for j in range(m):
            s2_freq[s2[j]] += 1
            if j - i + 1 > n:
                s2_freq[s2[i]] -= 1
                if s2_freq[s2[i]] == 0:
                    del s2_freq[s2[i]]
                i += 1
            if s1_freq == s2_freq:
                return True
        
        return False
