class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mp = defaultdict(int)
        for num in nums:
            r = ((num % value) + value) % value
            mp[r] += 1
        MEX = 0
        while mp[MEX % value] > 0:
            mp[MEX % value] -= 1
            MEX += 1
        return MEX