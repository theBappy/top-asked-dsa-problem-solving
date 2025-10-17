/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function (s, k) {
    const counts = {}
    let left = 0, right = 0
    let max_len = 0
    let max_count = 0
    while (right < s.length) {
        counts[s[right]] = (counts[s[right]] || 0) + 1;
        max_count = Math.max(max_count, counts[s[right]])
        while (max_count + k < right - left + 1) {
            counts[s[left]] -= 1
            left += 1
        }
        max_len = Math.max(max_len, right - left + 1)
        right += 1
    }
    return max_len
};prac