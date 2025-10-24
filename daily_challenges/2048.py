class Solution:
    def balanced(self, num: int) -> bool:
        freq = [0] * 10
        while num > 0:
            digit = num % 10
            freq[digit] += 1
            num //= 10
        for d in range(10):
            if freq[d] != 0 and freq[d] != d:
                return False
        return True

    def nextBeautifulNumber(self, n: int) -> int:
        for num in range(n + 1, 1224445):
            if self.balanced(num):
                return num
        return -1