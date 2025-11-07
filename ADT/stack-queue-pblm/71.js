/**
 * @param {string} path
 * @return {string}
 */
var simplifyPath = function (path) {
    const tokens = path.split("/")
    const stack = []
    for (const token of tokens) {
        if (token === "" || token === ".") {
            continue
        }
        if (token !== "..") {
            stack.push(token)
        } else if (stack.length > 0) {
            stack.pop()
        }
    }
    let result = ""
    while (stack.length) {
        result = "/" + stack.pop() + result
    }
    if (result.length === 0) {
        result = "/"
    }
    return result
};