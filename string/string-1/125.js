function isPalindrome(s) {
    let left = 0;
    let right = s.length - 1;
    while (left < right) {
        while (left < right && !/[a-zA-Z0-9]/.test(s.charAt(left))) {
            left++;
        }
        while (left < right && !/[a-zA-Z0-9]/.test(s.charAt(right))) {
            right--;
        }
        if (s.charAt(left).toLowerCase() !== s.charAt(right).toLowerCase()) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
