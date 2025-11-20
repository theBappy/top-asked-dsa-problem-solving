class Solution:
    def buildST(self, i: int, l: int, r: int, baskets: List[int], segmentTree: List[int]) -> None:
        if l == r:
            segmentTree[i] = baskets[l]
            return
        mid = l + (r - l) // 2
        self.buildST(2 * i + 1, l, mid, baskets, segmentTree)
        self.buildST(2 * i + 2, mid + 1, r, baskets, segmentTree)
        segmentTree[i] = max(segmentTree[2 * i + 1], segmentTree[2 * i + 2])

    def query(self, i: int, l: int, r: int, segmentTree: List[int], fruit: int) -> bool:
        if segmentTree[i] < fruit:
            return False
        if l == r:
            segmentTree[i] = -1
            return True
        mid = l + (r - l) // 2
        placed = False
        if segmentTree[2 * i + 1] >= fruit:
            placed = self.query(2 * i + 1, l, mid, segmentTree, fruit)
        else:
            placed = self.query(2 * i + 2, mid + 1, r, segmentTree, fruit)
        segmentTree[i] = max(segmentTree[2 * i + 1], segmentTree[2 * i + 2])
        return placed

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        segmentTree = [0] * (4 * n)
        self.buildST(0, 0, n - 1, baskets, segmentTree)

        unplaced = 0
        for fruit in fruits:
            if not self.query(0, 0, n - 1, segmentTree, fruit):
                unplaced += 1
        return unplaced