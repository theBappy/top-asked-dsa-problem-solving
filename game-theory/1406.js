


/**
 * @param {number[]} stoneValue
 * @return {string}
 */
var stoneGameIII = function (stoneValue) {
    const n = stoneValue.length;
    const t = new Array(n + 1).fill(-1);

    function solve(i) {
        if (i === n) {
            return 0;
        }

        if (t[i] !== -1) {
            return t[i];
        }

        t[i] = stoneValue[i] - solve(i + 1);

        if (i + 1 < n) {
            t[i] = Math.max(t[i], stoneValue[i] + stoneValue[i + 1] - solve(i + 2));
        }

        if (i + 2 < n) {
            t[i] = Math.max(t[i], stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - solve(i + 3));
        }

        return t[i];
    }

    const diff = solve(0);

    return diff > 0 ? "Alice" : diff < 0 ? "Bob" : "Tie";

};