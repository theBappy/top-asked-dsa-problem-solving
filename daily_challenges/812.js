/**
 * @param {number[][]} points
 * @return {number}
 */
var largestTriangleArea = function (points) {
    function shoeLace(p1, p2, p3) {
        const [x1, y1] = p1
        const [x2, y2] = p2
        const [x3, y3] = p3
        return 0.5 * Math.abs(
            x1 * (y2 - y3) +
            x2 * (y3 - y1) +
            x3 * (y1 - y2)
        )
    }
    let maxArea = 0.0
    const n = points.length
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            for (let k = j + 1; k < n; k++) {
                maxArea = Math.max(maxArea, shoeLace(points[i], points[j], points[k]))
            }
        }
    }
    return maxArea
};