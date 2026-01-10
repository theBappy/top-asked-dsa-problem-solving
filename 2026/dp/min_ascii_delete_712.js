/**
 * @param {string} s1
 * @param {string} s2
 * @return {number}
 */
var minimumDeleteSum = function (s1, s2) {
    const m = s1.length;
    const n = s2.length;
    const t = Array.from({ length: m + 1 }, () => Array(n + 1).fill(-1));
    const solve = (i, j) => {
        if (i >= m && j >= n) {
            return 0;
        }
        if (t[i][j] !== -1) {
            return t[i][j];
        }
        if (i >= m) {
            return t[i][j] = s2.charCodeAt(j) + solve(i, j + 1);
        } else if (j >= n) {
            return t[i][j] = s1.charCodeAt(i) + solve(i + 1, j);
        }
        let delete_i = s1.charCodeAt(i) + solve(i + 1, j);
        let delete_j = s2.charCodeAt(j) + solve(i, j + 1);
        let options = [delete_i, delete_j];
        if (s1[i] === s2[j]) {
            options.push(solve(i + 1, j + 1));
        }
        t[i][j] = Math.min(...options);
        return t[i][j];
    };
    return solve(0, 0);
};