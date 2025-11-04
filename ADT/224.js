/**
 * @param {string} s
 * @return {number}
 */
var calculate = function (s) {
    const st = [];
    let number = 0;
    let result = 0;
    let sign = 1;
    for (const char of s) {
        if (!isNaN(char) && char !== ' ') {
            number = (number * 10) + Number(char);
        } else if (char === '+') {
            result += number * sign;
            number = 0;
            sign = 1;
        } else if (char === '-') {
            result += number * sign;
            number = 0;
            sign = -1;
        } else if (char === '(') {
            st.push(result);
            st.push(sign);
            result = 0;
            number = 0;
            sign = 1;
        } else if (char === ')') {
            result += number * sign;
            number = 0;
            const stack_sign = st.pop();
            const last_result = st.pop();
            result = result * stack_sign + last_result;
        }
    }
    result += number * sign;
    return result;
};