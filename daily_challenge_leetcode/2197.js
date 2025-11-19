function gcd(a, b) {
    while (b !== 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}
var replaceNonCoprimes = function(nums) {
    const result = [];
    for (let num of nums) {
        while (result.length > 0) {
            let prev = result[result.length - 1];
            let curr = num;
            let GCD = gcd(prev, curr);
            if (GCD === 1) {
                break;
            }
            let LCM = (prev / GCD) * curr;
            num = LCM;
            result.pop();
        }
        result.push(num);
    }
    return result;
};