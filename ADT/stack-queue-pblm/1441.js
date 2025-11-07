/**
 * @param {number[]} target
 * @param {number} n
 * @return {string[]}
 */
var buildArray = function (target, n) {
    let stream = 1
    let i = 0
    const result = []
    while (i < target.length && stream <= n) {
        result.push("Push")
        if (target[i] === stream) {
            i++
        } else {
            result.push("Pop")
        }
        stream++
    }
    return result
};