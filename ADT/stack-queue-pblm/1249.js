

/**
 * @param {string} s
 * @return {string}
 */
var minRemoveToMakeValid = function (s) {
    const n = s.length
    const st = []
    const remove_idx = new Set()
    for (let i = 0; i < n; i++) {
        if (s[i] === '(') {
            st.push(i)
        } else if (s[i] === ')') {
            if (st.length === 0) {
                remove_idx.add(i)
            } else {
                st.pop()
            }
        }
    }
    while (st.length > 0) {
        remove_idx.add(st.pop())
    }
    let result = ""
    for (let i = 0; i < n; i++) {
        if (!remove_idx.has(i)) {
            result += s[i]
        }
    }
    return result
};