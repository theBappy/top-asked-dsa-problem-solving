/**
 * @param {string} bottom
 * @param {string[]} allowed
 * @return {boolean}
 */
var pyramidTransition = function(bottom, allowed) {

    // Map to store allowed transitions
    // "AB" -> ["C", "D", ...]
    const mp = new Map();

    for (const pattern of allowed) {
        const pair = pattern.substring(0, 2);
        const top = pattern[2];

        if (!mp.has(pair)) {
            mp.set(pair, []);
        }
        mp.get(pair).push(top);
    }

    // Memoization map
    const dp = new Map();

    /**
     * DFS + Backtracking helper
     * @param {string} curr - current row
     * @param {number} idx - current index in curr
     * @param {string} above - row being built above
     * @returns {boolean}
     */
    const solve = (curr, idx, above) => {

        // If pyramid reaches the top
        if (curr.length === 1) {
            return true;
        }

        // Create memoization key
        const key = `${curr}_${idx}_${above}`;
        if (dp.has(key)) {
            return dp.get(key);
        }

        // Finished current row, move to above row
        if (idx === curr.length - 1) {
            const result = solve(above, 0, "");
            dp.set(key, result);
            return result;
        }

        // Take adjacent pair
        const pair = curr.substring(idx, idx + 2);

        // If no allowed transition
        if (!mp.has(pair)) {
            dp.set(key, false);
            return false;
        }

        // Try all possible blocks
        for (const ch of mp.get(pair)) {
            // DO → add character to above row
            if (solve(curr, idx + 1, above + ch)) {
                dp.set(key, true);
                return true;
            }
        }

        // None worked
        dp.set(key, false);
        return false;
    };

    return solve(bottom, 0, "");
};


// Bit-mask + dfs
var pyramidTransition = function(bottom, allowed) {

    // trans[a][b] = bitmask of possible blocks above
    const trans = Array.from({ length: 7 }, () => Array(7).fill(0));

    // Build transition table
    for (const p of allowed) {
        const a = p.charCodeAt(0) - 65;
        const b = p.charCodeAt(1) - 65;
        const c = p.charCodeAt(2) - 65;
        trans[a][b] |= (1 << c);
    }

    // Convert bottom row to bitmasks
    let row = [];
    for (const ch of bottom) {
        row.push(1 << (ch.charCodeAt(0) - 65));
    }

    const memo = new Map();

    const dfs = (row) => {
        if (row.length === 1) return true;

        const key = row.join(",");
        if (memo.has(key)) return memo.get(key);

        // Build next row possibilities
        const next = [];

        const build = (idx, path) => {
            if (idx === row.length - 1) {
                next.push([...path]);
                return;
            }

            for (let a = 0; a < 7; a++) {
                if (!(row[idx] & (1 << a))) continue;

                for (let b = 0; b < 7; b++) {
                    if (!(row[idx + 1] & (1 << b))) continue;

                    let mask = trans[a][b];
                    while (mask) {
                        const bit = mask & -mask;
                        mask -= bit;
                        path.push(bit);
                        build(idx + 1, path);
                        path.pop();
                    }
                }
            }
        };

        build(0, []);

        for (const nxt of next) {
            if (dfs(nxt)) {
                memo.set(key, true);
                return true;
            }
        }

        memo.set(key, false);
        return false;
    };

    return dfs(row);
};