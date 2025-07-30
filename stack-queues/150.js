class Solution{
    constructor(){
        this.operators = {
            '+' : (a,b) => a + b,
            '-' : (a,b) => a - b,
            '*' : (a,b) => a * b,
            '/' : (a,b) => Math.trunc(a / b),
         }
    }
    evalRPN(tokens){
        const stack = []
        for(const token of tokens){
            if(token in this.operators){
                const b = stack.pop()
                const a = stack.pop()
                stack.push(this.operators[token](a,b))
            }else{
                            // parseInt(string, radix)
                stack.push(parseInt(token, 10))
            }
        }
        return stack.pop()
    }
}