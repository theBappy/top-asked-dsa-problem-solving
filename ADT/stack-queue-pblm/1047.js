/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicates = function (s) {
    const st = []
    for (let i = s.length - 1; i >= 0; i--) {
        if (st.length === 0 || st[st.length - 1] !== s[i]) {
            st.push(s[i])
        } else {
            st.pop()
        }
    }
    let result = ''
    while (st.length) {
        result += st.pop()
    }
    return result
};