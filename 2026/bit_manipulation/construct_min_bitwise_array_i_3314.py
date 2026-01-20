class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            found = False
            for x in range(num):
                if (x | (x + 1)) == num:
                    result.append(x)
                    found = True
                    break
            if not found:
                result.append(-1)
        return result



class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if num == 2:
                result.append(-1)
                continue
            found = False
            for j in range(1, 32):
                if (num & (1 << j)) > 0:
                    continue
                result.append(num ^ (1 << (j - 1)))
                found = True
                break
            if not found:
                result.append(-1)
        return result
        