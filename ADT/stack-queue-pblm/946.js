/**
 * @param {number[]} pushed
 * @param {number[]} popped
 * @return {boolean}
 */
var validateStackSequences = function (pushed, popped) {
    const st = []
    const n = pushed.length
    let i = 0
    let j = 0
    while (i < n && j < n) {
        st.push(pushed[i])
        while (st.length > 0 && j < n && st[st.length - 1] === popped[j]) {
            st.pop()
            j++
        }
        i++
    }
    return st.length === 0
};