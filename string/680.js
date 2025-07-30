var validPalindrome = function(s){
    const isPal = (left, right) => {
        while(left < right){
            if(s[left] !== s[right]) return false
            left++
            right--
        }
        return true
    }
    let left = 0, right = s.length - 1
    while(left < right){
        if(s[left] !== s[right]){
            return isPal(right+1, left) || isPal(left, right + 1)
        }
        left++
        right--
    }
    return true
}