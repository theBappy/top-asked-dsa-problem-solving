/**
 * @param {number[]} fruits
 * @param {number[]} baskets
 * @return {number}
 */
var numOfUnplacedFruits = function (fruits, baskets) {
    const n = fruits.length;
    let unplaced = 0;
    for (let i = 0; i < n; i++) {
        let placed = false;
        for (let j = 0; j < n; j++) {
            if (fruits[i] <= baskets[j]) {
                placed = true;
                baskets[j] = -1;
                break;
            }
        }
        if (!placed) {
            unplaced += 1;
        }
    }
    return unplaced;
};