function minimumOneBitOperations(n){
    if(n === 0){
        return 0
    }
    const F = new Array(31).fill(0)

    F[0] = 1
    for(let i = 1; i < 31; i++){
        F[i] = 2 * F[i-1] + 1
    }

    let result = 0
    let sign = 1
    for(let i = 30; i >= 0; i--){
        const ith_bit = (1 << i) & n
        if(ith_bit === 0){
            continue
        }
        if(sign > 0){
            result += F[i]
        }else{
            result -= F[i]
        }
        sign *= -1
    }
    return result
}