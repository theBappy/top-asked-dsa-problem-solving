class Solution {
    buildSegmentTree(i, l, r, st, heights) {
        if (l === r) {
            st[i] = l;
            return;
        }

        let mid = Math.floor((l + r) / 2);

        this.buildSegmentTree(2 * i + 1, l, mid, st, heights);
        this.buildSegmentTree(2 * i + 2, mid + 1, r, st, heights);

        let leftIdx = st[2 * i + 1];
        let rightIdx = st[2 * i + 2];

        st[i] =
            heights[leftIdx] >= heights[rightIdx] ? leftIdx : rightIdx;
    }

    constructST(heights, n) {
        let st = new Array(4 * n).fill(-1);
        this.buildSegmentTree(0, 0, n - 1, st, heights);
        return st;
    }

    queryST(start, end, i, l, r, st, heights) {
        if (l > end || r < start) return -1;
        if (l >= start && r <= end) return st[i];

        let mid = Math.floor((l + r) / 2);

        let leftIdx = this.queryST(start, end, 2 * i + 1, l, mid, st, heights);
        let rightIdx =
            this.queryST(start, end, 2 * i + 2, mid + 1, r, st, heights);

        if (leftIdx === -1) return rightIdx;
        if (rightIdx === -1) return leftIdx;

        return heights[leftIdx] >= heights[rightIdx] ? leftIdx : rightIdx;
    }

    RMIQ(st, heights, n, start, end) {
        return this.queryST(start, end, 0, 0, n - 1, st, heights);
    }

    leftmostBuildingQueries(heights, queries) {
        let n = heights.length;
        let st = this.constructST(heights, n);

        let result = [];

        for (let q of queries) {
            let a = q[0], b = q[1];

            let minIdx = Math.min(a, b);
            let maxIdx = Math.max(a, b);

            if (minIdx === maxIdx || heights[maxIdx] > heights[minIdx]) {
                result.push(maxIdx);
                continue;
            }

            let l = maxIdx + 1;
            let r = n - 1;
            let best = Number.MAX_SAFE_INTEGER;

            while (l <= r) {
                let mid = Math.floor((l + r) / 2);
                let idx = this.RMIQ(st, heights, n, l, mid);

                if (idx !== -1 &&
                    heights[idx] > Math.max(heights[minIdx], heights[maxIdx])) {
                    best = Math.min(best, idx);
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            }

            result.push(best === Number.MAX_SAFE_INTEGER ? -1 : best);
        }

        return result;
    }
}
