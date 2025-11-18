
class NumArray {
    constructor(nums) {
        this.n = nums.length;
        this.st = new Array(4 * this.n).fill(0);
        this.build(0, 0, this.n - 1, nums);
    }

    build(i, l, r, nums) {
        if (l === r) {
            this.st[i] = nums[l];
            return;
        }

        const mid = (l + r) >> 1;
        this.build(2 * i + 1, l, mid, nums);
        this.build(2 * i + 2, mid + 1, r, nums);

        this.st[i] = this.st[2 * i + 1] + this.st[2 * i + 2];
    }

    updateTree(i, l, r, index, val) {
        if (l === r) {
            this.st[i] = val;
            return;
        }

        const mid = (l + r) >> 1;

        if (index <= mid) {
            this.updateTree(2 * i + 1, l, mid, index, val);
        } else {
            this.updateTree(2 * i + 2, mid + 1, r, index, val);
        }

        this.st[i] = this.st[2 * i + 1] + this.st[2 * i + 2];
    }

    query(i, l, r, ql, qr) {
        // no overlap
        if (r < ql || l > qr) return 0;

        // complete overlap
        if (l >= ql && r <= qr) return this.st[i];

        const mid = (l + r) >> 1;

        return (
            this.query(2 * i + 1, l, mid, ql, qr) +
            this.query(2 * i + 2, mid + 1, r, ql, qr)
        );
    }

    update(index, val) {
        this.updateTree(0, 0, this.n - 1, index, val);
    }

    sumRange(left, right) {
        return this.query(0, 0, this.n - 1, left, right);
    }
}
