// Tc = O(n)
// Sc = O(2566) => for valid ascii character // constant => O(1)

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function (s, t) {
    const mp1 = new Map();
        const mp2 = new Map();
        const m = s.length;
        for (let i = 0; i < m; i++) {
            const ch1 = s[i];
            const ch2 = t[i];
            if ((mp1.has(ch1) && mp1.get(ch1) !== ch2) || (mp2.has(ch2) && mp2.get(ch2) !== ch1)) {
                return false;
            }
            mp1.set(ch1, ch2);
            mp2.set(ch2, ch1);
        }
        return true;
};