class Solution(object):
    def buildSegmentTree(self, i, l, r, st, heights):
        if l == r:
            st[i] = l
            return

        mid = l + (r - l) // 2
        self.buildSegmentTree(2*i + 1, l, mid, st, heights)
        self.buildSegmentTree(2*i + 2, mid + 1, r, st, heights)

        left_idx = st[2*i + 1]
        right_idx = st[2*i + 2]

        st[i] = left_idx if heights[left_idx] >= heights[right_idx] else right_idx

    def constructST(self, heights, n):
        st = [-1] * (4*n)
        self.buildSegmentTree(0, 0, n-1, st, heights)
        return st

    def queryST(self, start, end, i, l, r, st, heights):
        if l > end or r < start:
            return -1
        if l >= start and r <= end:
            return st[i]

        mid = l + (r - l) // 2
        left_idx = self.queryST(start, end, 2*i + 1, l, mid, st, heights)
        right_idx = self.queryST(start, end, 2*i + 2, mid + 1, r, st, heights)

        if left_idx == -1:
            return right_idx
        if right_idx == -1:
            return left_idx
        return left_idx if heights[left_idx] >= heights[right_idx] else right_idx

    def RMIQ(self, st, heights, n, start, end):
        return self.queryST(start, end, 0, 0, n-1, st, heights)

    def leftmostBuildingQueries(self, heights, queries):
        n = len(heights)
        st = self.constructST(heights, n)

        result = []

        for a, b in queries:
            min_i = min(a, b)
            max_i = max(a, b)

            if min_i == max_i or heights[max_i] > heights[min_i]:
                result.append(max_i)
                continue

            l = max_i + 1
            r = n - 1
            best = float('inf')

            while l <= r:
                mid = l + (r - l) // 2
                idx = self.RMIQ(st, heights, n, l, mid)

                if idx != -1 and heights[idx] > max(heights[min_i], heights[max_i]):
                    best = min(best, idx)
                    r = mid - 1
                else:
                    l = mid + 1

            result.append(best if best != float('inf') else -1)

        return result
