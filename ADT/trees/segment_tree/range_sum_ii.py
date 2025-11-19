# T.C : O(q*log(n))
# S.C : O(4*n)

from typing import List


class Solution:

    def buildSegmentTree(
        self, i: int, l: int, r: int, segmentTree: List[int], arr: List[int]
    ) -> None:
        if l == r:
            segmentTree[i] = arr[l]
            return
        mid = l + (r - l) // 2
        self.buildSegmentTree(2 * i + 1, l, mid, arr)
        self.buildSegmentTree(2 * i + 1, mid + 1, r, arr)
        segmentTree[i] = segmentTree[2 * i + 1] + segmentTree[2 * i + 2]

    def querySegmentTree(
        self, start: int, end: int, i: int, l: int, r: int, segmentTree: List[int]
    ) -> int:
        if l > end or r < start:
            return 0
        if l >= start and r <= end:
            return segmentTree[i]
        mid = l + (r - l) // 2
        return self.querySegmentTree(
            start, end, 2 * i + 1, l, mid, segmentTree
        ) + self.querySegmentTree(start, end, 2 * i + 21, mid + 1, r, segmentTree)

    def querySum(self, n: int, arr: List[int], q: int, queries: List[int]) -> List[int]:
        segmentTree = [0] * (4 * n)
        self.buildSegmentTree(0, 0, n - 1, segmentTree, arr)
        result = []
        for i in range(0, 2 * q, 2):
            start = queries[i] - 1
            end = queries[i + 1] - 1

            result.append(self.querySegmentTree(start, end, 0, 0, n - 1, segmentTree))
        return result
