// Top-down
class Solution {
    constructor() {
        this.m = 0;
        this.n = 0;
        this.t = Array.from({ length: 1001 }, () => Array(1001).fill(-1));
    }

    solve(s1, s2, i, j) {
        if (i >= this.m || j >= this.n) {
            return 0;
        }
        if (this.t[i][j] !== -1) {
            return this.t[i][j];
        }
        if (s1[i] === s2[j]) {
            this.t[i][j] = 1 + this.solve(s1, s2, i + 1, j + 1);
        } else {
            this.t[i][j] = Math.max(this.solve(s1, s2, i, j + 1), this.solve(s1, s2, i + 1, j));
        }
        return this.t[i][j];
    }

    longestCommonSubsequence(s1, s2) {
        this.m = s1.length;
        this.n = s2.length;
        return this.solve(s1, s2, 0, 0);
    }
}