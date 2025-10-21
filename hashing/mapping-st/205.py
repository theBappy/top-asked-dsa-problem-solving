class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp1 = {}
        mp2 = {}
        m = len(s)
        for i in range(m):
            ch1 = s[i]
            ch2 = t[i]
            if (ch1 in mp1 and mp1[ch1] != ch2) or (ch2 in mp2 and mp2[ch2] != ch1):
                return False
            mp1[ch1] = ch2
            mp2[ch2] = ch1
        return True