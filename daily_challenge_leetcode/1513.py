class Solution:
    M = int(1e9 + 7)

    def numSub(self, s: str) -> int:
        result = 0
        count1 = 0
        for ch in s:
            if ch == '1':
                count1 += 1
            else:
                result = (result + count1 * (count1 + 1) // 2) % self.M
                count1 = 0
        # adding the last group of 1's
        result = (result + count1 * (count1 + 1) // 2) % self.M
        return result


class Solution:
    M = int(1e9 + 7)

    def numSub(self, s: str) -> int:
        result = 0
        count1 = 0
        for ch in s:
            if ch == '1':
                count1 += 1
                result = (result + count1) % self.M
            else:
                count1 = 0
        return result