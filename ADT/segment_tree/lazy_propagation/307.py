class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.st = [0] * (4 * self.n)
        self._buildST(0, 0, self.n - 1, nums)

    def _buildST(self, i: int, l: int, r: int, nums: list[int]):
        if l == r:
            self.st[i] = nums[l]
            return
        mid = (l + r) // 2
        self._buildST(2 * i + 1, l, mid, nums)
        self._buildST(2 * i + 2, mid + 1, r, nums)
        self.st[i] = self.st[2 * i + 1] + self.st[2 * i + 2]

    def _updateST(self, index: int, val: int, i: int, l: int, r: int):
        if l == r:
            self.st[i] = val
            return
        mid = (l + r) // 2
        if index <= mid:
            self._updateST(index, val, 2 * i + 1, l, mid)
        else:
            self._updateST(index, val, 2 * i + 2, mid + 1, r)
        self.st[i] = self.st[2 * i + 1] + self.st[2 * i + 2]

    def _query(self, start: int, end: int, i: int, l: int, r: int) -> int:
        if r < start or l > end:
            return 0
        if l >= start and r <= end:
            return self.st[i]
        mid = (l + r) // 2
        return self._query(start, end, 2 * i + 1, l, mid) + \
               self._query(start, end, 2 * i + 2, mid + 1, r)

    def update(self, index: int, val: int) -> None:
        self._updateST(index, val, 0, 0, self.n - 1)

    def sumRange(self, left: int, right: int) -> int:
        return self._query(left, right, 0, 0, self.n - 1)