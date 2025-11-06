/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
    const st = [];

    for (const ch of s) {
        if (st.length === 0 || ch === '(' || ch === '{' || ch === '[') {
            st.push(ch);
            continue;
        }

        if (ch === ')') {
            if (st[st.length - 1] === '(')
                st.pop();
            else
                return false;
        } else if (ch === '}') {
            if (st[st.length - 1] === '{')
                st.pop();
            else
                return false;
        } else if (ch === ']') {
            if (st[st.length - 1] === '[')
                st.pop();
            else
                return false;
        }
    }

    return st.length === 0;
};



/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
    const st = []
    for (const ch of s) {
        if (ch === '(') {
            st.push(')')
        } else if (ch === '{') {
            st.push('}')
        } else if (ch === '[') {
            st.push(']')
        } else if (st.length === 0 || st[st.length - 1] !== ch) {
            return false
        } else {
            st.pop()
        }
    }
    return st.length === 0
};