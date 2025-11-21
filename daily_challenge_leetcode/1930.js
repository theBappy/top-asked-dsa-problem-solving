/**
 * @param {string} s
 * @return {number}
 */
var countPalindromicSubsequence = function (s) {
    const n = s.length
    const unique_letters = new Set(s)
    let result = 0
    for (const letter of unique_letters) {
        let first_idx = - 1
        let last_idx = - 1
        for (let i = 0; i < n; i++) {
            if (s[i] === letter) {
                if (first_idx === - 1) {
                    first_idx = i
                }
                last_idx = i
            }
        }
        const st = new Set()
        for (let middle = first_idx + 1; middle <= last_idx - 1; middle++) {
            st.add(s[middle])
        }
        result += st.size
    }
    return result
};