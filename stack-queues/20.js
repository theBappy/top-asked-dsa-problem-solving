class Solution {
    isValid(s){
        const stack = []
        for(let ch of s){
            if(stack.length === 0 || '({['.includes(ch)){
                stack.push(ch)
                continue
            }
            if(ch == ')'){
                if(stack.length > 0 && stack[stack.length-1] === '('){
                    stack.pop()
                }else{
                    return false
                }
            }else if(ch === '}'){
                if(stack.length > 0 && stack[stack.length -1] === '{'){
                    stack.pop()
                }else{
                    return false
                }
            }else if(ch === ']'){
                if(stack.length >0 && stack[stack.length - 1] === '['){
                    stack.pop()
                }else{
                    return false
                }
            }
        }
        return stack.length === 0
    }
}