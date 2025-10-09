class Solution {
    constructor() {
        this.t = null;
    }

    solve(s, l, r) {
        if (l >= r) {
            return true;
        }

        if (this.t[l][r] !== null) {
            return this.t[l][r];
        }

        if (s[l] === s[r]) {
            this.t[l][r] = this.solve(s, l + 1, r - 1);
            return this.t[l][r];
        }

        this.t[l][r] = false;
        return false;
    }

    longestPalindrome(s) {
        const n = s.length;
        this.t = Array.from({ length: n }, () => Array(n).fill(null));

        let maxlen = -Infinity;
        let startingIndex = 0;

        for (let i = 0; i < n; i++) {
            for (let j = i; j < n; j++) {
                if (this.solve(s, i, j)) {
                    if (j - i + 1 > maxlen) {
                        startingIndex = i;
                        maxlen = j - i + 1;
                    }
                }
            }
        }

        return s.substring(startingIndex, startingIndex + maxlen);
    }
}