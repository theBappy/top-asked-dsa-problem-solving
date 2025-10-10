/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function (s, p) {
    const solve = (i, j, t) => {
        if (j === p.length) {
            return i === s.length;
        }
        if (t[i][j] !== -1) {
            return t[i][j];
        }
        const firstMatch = i < s.length && (p[j] === s[i] || p[j] === '.');
        let res;
        if (j + 1 < p.length && p[j + 1] === '*') {
            const notUse = solve(i, j + 2, t);
            const use = firstMatch && solve(i + 1, j, t);
            res = notUse || use;
        } else {
            res = firstMatch && solve(i + 1, j + 1, t);
        }
        t[i][j] = res;
        return res;
    };
    const m = s.length, n = p.length;
    const t = Array.from({ length: m + 1 }, () => Array(n + 1).fill(-1));
    return solve(0, 0, t);
};