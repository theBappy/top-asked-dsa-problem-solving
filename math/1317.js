/**
 * @param {number} n
 * @return {number[]}
 */
var getNoZeroIntegers = function (n) {
    const check = (num) => {
        while (num) {
            if (num % 10 === 0) {
                return false
            }
            num = Math.floor(num / 10)
        }
        return true
    }
    for (let a = 1; a <= n - 1; a++) {
        b = n - a
        if (check(a) && check(b)) {
            return [a, b]
        }
    }
    return []
};



/**
 * @param {number} n
 * @return {number[]}
 */
var getNoZeroIntegers = function(n) {
    let a = n
    let b = 0
    let placeValue = 1
    while(n > 1){
        let take = 1
        if(n % 10 === 1){
            take = 2
        }
        a = a - (take * placeValue)
        b = b + (take * placeValue)
        n = Math.floor((n-take) / 10)
        placeValue *= 10
    }
    return [a,b]
};