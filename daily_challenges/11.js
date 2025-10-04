/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
    const n = height.length
    let maxArea = 0
    let i = 0, j = n - 1
    while (i < j) {
        let h = Math.min(height[i], height[j])
        let w = j - i
        let area = w * h
        if (height[i] > height[j]) {
            j--
        } else {
            i++
        }
        maxArea = Math.max(area, maxArea)
    }
    return maxArea
};