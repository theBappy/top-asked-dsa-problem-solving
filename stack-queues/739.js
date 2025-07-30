class Solution {
    dailyTemperatures(temp){
        const n = temp.length
        const stack = []
        const result = new Array(n).fill(0)

        for(let i = n-1; i>=0; i--){
            while(stack.length && temp[i] >= temp[stack[stack.length-1]]){
                stack.pop()
            }
            if(stack.length === 0){
                result[i] = 0
            }else{
                result[i] = stack[stack.length - 1] - i
            }
            stack.push(i)
        }
        return result
    }
}