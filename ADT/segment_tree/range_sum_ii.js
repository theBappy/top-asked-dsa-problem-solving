class Solution {
    buildSegmentTree(i, l, r, segmentTree, arr) {
        if (l === r) {
            segmentTree[i] = arr[l];
            return;
        }

        const mid = l + Math.floor((r - l) / 2);
        this.buildSegmentTree(2 * i + 1, l, mid, segmentTree, arr);
        this.buildSegmentTree(2 * i + 2, mid + 1, r, segmentTree, arr);
        segmentTree[i] = segmentTree[2 * i + 1] + segmentTree[2 * i + 2];
    }

    querySegmentTree(start, end, i, l, r, segmentTree) {
        if (l > end || r < start) {
            return 0;
        }

        if (l >= start && r <= end) {
            return segmentTree[i];
        }

        const mid = l + Math.floor((r - l) / 2);
        return this.querySegmentTree(start, end, 2 * i + 1, l, mid, segmentTree) +
               this.querySegmentTree(start, end, 2 * i + 2, mid + 1, r, segmentTree);
    }

    querySum(n, arr, q, queries) {
        const segmentTree = new Array(4 * n).fill(0);

        this.buildSegmentTree(0, 0, n - 1, segmentTree, arr);

        const result = [];
        for (let i = 0; i < 2 * q; i += 2) {
            const start = queries[i] - 1;   // Input is in 1-based indexing
            const end = queries[i + 1] - 1; // Input is in 1-based indexing

            result.push(this.querySegmentTree(start, end, 0, 0, n - 1, segmentTree));
        }

        return result;
    }
}