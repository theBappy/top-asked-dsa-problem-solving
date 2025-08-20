var maxUncrossedLines = function (nums1, nums2) {
        const m = nums1.length;
        const n = nums2.length;
        const t = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));
        
        for (let i = 0; i <= m; i++) {
            for (let j = 0; j <= n; j++) {
                if (i === 0 || j === 0) {
                    t[i][j] = 0;
                } else if (nums1[i - 1] === nums2[j - 1]) {
                    t[i][j] = 1 + t[i - 1][j - 1];
                } else {
                    t[i][j] = Math.max(t[i][j - 1], t[i - 1][j]);
                }
            }
        }
        return t[m][n];
};