/**
 * @param {number[]} people
 * @param {number} limit
 * @return {number}
 */
var numRescueBoats = function (people, limit) {
    people.sort((a, b) => a - b)
    let i = 0, j = people.length - 1
    let boats = 0
    while (i <= j) {
        if (people[j] + people[i] <= limit) {
            i++
            j--
        } else {
            j--
        }
        boats++
    }
    return boats
};