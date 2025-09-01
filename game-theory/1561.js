
/**
 * @param {number[]} piles
 * @return {number}
 */
var maxCoins = function(piles) {
    const n = piles.length
    let result = 0
    piles.sort((a, b) => a - b)
    let bob = 0
    let myself = n-2
    while(myself > bob){
        result += piles[myself]
        myself -= 2
        bob += 1
    }
    return result
};



var maxCoins = function(piles) {
    const n = piles.length
    let result = 0
    piles.sort((a, b) => a - b)
    for(let M = n / 3; M < n; M += 2){
        result += piles[M]
    }
    return result
};