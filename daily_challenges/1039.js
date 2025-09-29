var minScoreTriangulation = function (values) {
    const n = values.length;
    const t = Array.from({ length: n }, () => Array(n).fill(-1));

    const solve = (i, j) => {
        if (j - i + 1 < 3) {
            return 0;
        }
        if (t[i][j] !== -1) {
            return t[i][j];
        }
        let result = Number.MAX_SAFE_INTEGER;
        for (let k = i + 1; k < j; k++) {
            let wt = (values[i] * values[j] * values[k]) + solve(i, k) + solve(k, j);
            result = Math.min(result, wt);
        }
        t[i][j] = result;
        return result;
    };

    return solve(0, n - 1);
};
