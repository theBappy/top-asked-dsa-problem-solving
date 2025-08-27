var countBits = function(n) {
    const result = new Array(n + 1).fill(0);
    for (let i = 0; i <= n; i++) {
        result[i] = i.toString(2).split('0').join('').length;
    }
    return result;
};


var countBits = function(n) {
    const result = new Array(n+1).fill(0)
    if(n === 0) return result
    for(let i = 1; i <= n; i++){
        if(i % 2 == 1){
            result[i] = result[Math.floor(i / 2)] + 1
        }else{
            result[i] = result[Math.floor(i / 2)]
        }
    }
    return result
};