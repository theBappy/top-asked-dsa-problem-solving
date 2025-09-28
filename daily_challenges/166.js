/**
 * @param {number} numerator
 * @param {number} denominator
 * @return {string}
 */
var fractionToDecimal = function(numerator, denominator) {
    if(numerator === 0){
        return "0"
    }
    const result = []
    if(numerator * denominator < 0){
        result.push("-")
    }
    const absNum = Math.abs(numerator)
    const absDen = Math.abs(denominator)

    const integerDiv = Math.floor(absNum / absDen)
    result.push(integerDiv.toString())

    let remainder = absNum % absDen
    if(remainder === 0){
        return result.join('')
    }
    result.push('.')
    const mp = new Map()
    while(remainder !== 0){
        if(mp.has(remainder)){
            result.splice(mp.get(remainder), 0, '(');
            result.push(')')
            break
        }
        mp.set(remainder, result.length)
        remainder *= 10
        const digit = Math.floor(remainder / absDen)
        result.push(digit.toString())
        remainder %= absDen
    }
    return result.join('')
};