class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.t = [[-int(1e9)] * 501 for _ in range(501)]
        
    def solve(self, nums1: List[int], nums2: List[int], i: int, j: int) -> int:
        if i == self.m or j == self.n:
            return -100000000  # large negative number
        if self.t[i][j] != -int(1e9):
            return self.t[i][j] 
        val = nums1[i] * nums2[j]
        take_i_j = self.solve(nums1, nums2, i + 1, j+1) + val
        take_i = self.solve(nums1, nums2, i, j+1)
        take_j = self.solve(nums1, nums2, i+1, j)
        self.t[i][j] = max(val, take_i_j, take_i, take_j)
        return self.t[i][j]

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        self.m = len(nums1)
        self.n = len(nums2)
        for i in range(501):
            for j in range(501):
                self.t[i][j] = -int(1e9)
        return self.solve(nums1, nums2, 0, 0)
