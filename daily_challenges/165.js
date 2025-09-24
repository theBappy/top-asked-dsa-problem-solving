/**
 * @param {string} version1
 * @param {string} version2
 * @return {number}
 */
var compareVersion = function (version1, version2) {
    const getTokens = (version) => {
        return version.split(".")
    }
    const v1 = getTokens(version1)
    const v2 = getTokens(version2)
    const m = v1.length, n = v2.length
    let i = 0
    while (i < m || i < n) {
        const a = i < m ? parseInt(v1[i], 10) : 0
        const b = i < n ? parseInt(v2[i], 10) : 0
        if (a < b) {
            return -1
        } else if (a > b) {
            return 1
        }
        i += 1

    }
    return 0
};