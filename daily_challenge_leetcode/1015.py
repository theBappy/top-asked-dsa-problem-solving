class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k == 1:
            return 1
        num = 0
        for length in range(1, k+1):
            num = (num * 10 + 1) % k
            if num == 0:
                return length
        return -1
