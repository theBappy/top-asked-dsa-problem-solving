/**
 * @param {string} colors
 * @param {number[]} neededTime
 * @return {number}
 */
var minCost = function (colors, neededTime) {
    const n = colors.length
    let time = 0
    let prevMax = 0
    for (let i = 0; i < n; i++) {
        if (i > 0 && colors[i] !== colors[i - 1]) {
            prevMax = 0
        }
        const curr = neededTime[i]
        time += Math.min(prevMax, curr)
        prevMax = Math.max(prevMax, curr)
    }
    return time
};