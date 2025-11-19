/**
 * @param {number} n
 * @return {number}
 */
var nextBeautifulNumber = function (n) {
    const balanced = (num) => {
        const freq = new Array(10).fill(0)
        while (num > 0) {
            const digit = num % 10
            freq[digit]++
            num = Math.floor(num / 10)
        }
        for (let d = 0; d < 10; d++) {
            if (freq[d] !== 0 && freq[d] !== d) {
                return false
            }
        }
        return true
    }
    for (let num = n + 1; num <= 1224444; num++) {
        if (balanced(num)) {
            return num;
        }
    }
    return -1;
};

