

/**
 * @param {string} s
 * @return {number}
 */
var minSwaps = function (s) {
    const st = []
    for (const ch of s) {
        if (ch === '[') {
            st.push(ch)
        } else if (st.length > 0) {
            st.pop()
        }
    }
    return Math.floor((st.length + 1) / 2)
};


/**
 * @param {string} s
 * @return {number}
 */
var minSwaps = function (s) {
    let size = 0
    for (const ch of s) {
        if (ch === '[') {
            size++
        } else if (size !== 0) {
            size--
        }
    }
    return Math.floor((size + 1) / 2)
};