
// Manacher's Algo
/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
    if (!s || s.length === 0) return "";

    const transform = (s) => {
        let t = '^'; 
        for (let ch of s) {
            t += `#${ch}`;
        }
        t += '#$'; 
        return t;
    };

    const t = transform(s);
    const n = t.length;
    const p = new Array(n).fill(0);
    let center = 0, right = 0;
    let maxLen = 0, centerIndex = 0;

    for (let i = 1; i < n - 1; i++) {
        const mirror = 2 * center - i;

        if (i < right)
            p[i] = Math.min(right - i, p[mirror]);

        while (t[i + 1 + p[i]] === t[i - 1 - p[i]])
            p[i]++;
        if (i + p[i] > right) {
            center = i;
            right = i + p[i];
        }

        if (p[i] > maxLen) {
            maxLen = p[i];
            centerIndex = i;
        }
    }

    const start = Math.floor((centerIndex - maxLen) / 2);
    return s.substring(start, start + maxLen);
};

// expansion from center
/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
    const n = s.length;
    if (n === 0) return ''
    let start = 0, maxLen = 0
    for (let i = 0; i < n; i++) {
        for (let j = 0; j <= 1; j++) {
            let low = i
            let high = i + j
            while (low >= 0 && high < n && s[low] === s[high]) {
                const currLen = high - low + 1
                if (currLen > maxLen) {
                    maxLen = currLen
                    start = low
                }
                low--
                high++
            }
        }
    }
    return s.substring(start, start + maxLen)
};
