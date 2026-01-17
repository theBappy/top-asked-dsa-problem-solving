/**
 * @param {number[][]} bottomLeft
 * @param {number[][]} topRight
 * @return {number}
 */
var largestSquareArea = function (bottomLeft, topRight) {
    const n = bottomLeft.length;

    let maxSide = 0;

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            // Width
            const topRightX = Math.min(topRight[i][0], topRight[j][0]);
            const bottomLeftX = Math.max(bottomLeft[i][0], bottomLeft[j][0]);

            const width = topRightX - bottomLeftX;

            // Height
            const topRightY = Math.min(topRight[i][1], topRight[j][1]);
            const bottomLeftY = Math.max(bottomLeft[i][1], bottomLeft[j][1]);

            const height = topRightY - bottomLeftY;

            const side = Math.min(width, height);

            maxSide = Math.max(maxSide, side);
        }
    }
    return maxSide * maxSide
};