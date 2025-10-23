class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        while n > 2:
            s = ''.join(str((int(s[i]) + int(s[i + 1])) % 10) for i in range(n-1))
            n -= 1
        return s[0] == s[1]