/**
 * @param {string} s
 * @param {number} a
 * @param {number} b
 * @return {string}
 */
var findLexSmallestString = function(s, a, b) {
    let smallestString = s;
    const visited = new Set();
    const queue = [];
    queue.push(s);
    visited.add(s);
    
    while (queue.length > 0) {
        const curr = queue.shift();
        if (curr < smallestString) {
            smallestString = curr;
        }
        
        let tempArr = curr.split("");
        for (let i = 1; i < tempArr.length; i += 2) {
            tempArr[i] = ((parseInt(tempArr[i], 10) + a) % 10).toString();
        }
        const added = tempArr.join("");
        if (!visited.has(added)) {
            visited.add(added);
            queue.push(added);
        }

        const rotated = curr.slice(-b) + curr.slice(0, curr.length - b);
        if (!visited.has(rotated)) {
            visited.add(rotated);
            queue.push(rotated);
        }
    }
    
    return smallestString;
};
