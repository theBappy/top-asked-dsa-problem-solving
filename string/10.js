class Solution {
    constructor() {
        this.t = Array.from({ length: 21 }, () => Array(21).fill(-1));
    }

    solve(i, j, s, p) {
        if (j === p.length) {
            return i === s.length;
        }
        if (this.t[i][j] !== -1) {
            return this.t[i][j];
        }
        let firstCharMatched = false;
        if (i < s.length && (p[j] === s[i] || p[j] === '.')) {
            firstCharMatched = true;
        }
        if (j + 1 < p.length && p[j + 1] === '*') {
            const notTake = this.solve(i, j + 2, s, p);
            const take = firstCharMatched && this.solve(i + 1, j, s, p);
            this.t[i][j] = notTake || take;
            return this.t[i][j];
        }
        this.t[i][j] = firstCharMatched && this.solve(i + 1, j + 1, s, p);
        return this.t[i][j];
    }

    isMatch(s, p) {
        this.t = Array.from({ length: 21 }, () => Array(21).fill(-1));
        return this.solve(0, 0, s, p);
    }
}