/**
 * @param {number} n
 * @return {number}
 */
var countOrders = function(n) {
    const mod = 1e9 + 7
    if(n===1){
        return 1
    }
    let result = 1
    for(let i = 2; i<=n; i++){
        const spaces = (i - 1) * 2 + 1
        const possibility = spaces * (Math.floor(spaces + 1)/2)
        result =  (result * possibility) % mod
    }
    return result

};