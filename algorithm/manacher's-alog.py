# Tc = O(n)
# Sc = O(n)

def transform(s):
    # Transform the input string by inserting '#' between characters
    # This helps to handle even-length palindromes uniformly
    temp = ['#']
    for ch in s:
        temp.append(ch)
        temp.append('#')
    return ''.join(temp)

    t = transform(s)              # Preprocessed string with '#' inserted
    n = len(t)                    # Length of the transformed string
    l = 0                         # Left boundary of the current palindrome
    r = 0                         # Right boundary of the current palindrome
    center = 0                    # Center index of the longest palindrome found
    max_len = 0                   # Length of the longest palindrome
    p = [0] * n                   # Array to store the radius (half-length) of palindromes centered at each index

    for i in range(1, n):
        # Determine the initial value of k (radius)
        if i > r:
            k = 0                # If current position is beyond right boundary, start fresh
        else:
            j = l + (r - i)      # Mirror position of i with respect to current palindrome center
            if j - p[j] > l:
                p[i] = p[j]      # Use the mirror’s value directly if within boundary
                continue
            else:
                k = r - i        # Otherwise, limit expansion to boundary

        # Try to expand palindrome centered at i
        while i - k >= 0 and i + k < n and t[i - k] == t[i + k]:
            k += 1
        k -= 1                  # One step back after mismatch

        p[i] = k                # Store the max expansion for center i

        # Update longest palindrome if needed
        if p[i] > max_len:
            max_len = p[i]
            center = i

        # Update current known palindrome boundaries if expanded further
        if i + k > r:
            l = i - k
            r = i + k

    # Calculate original string start index
    start = (center - max_len) // 2
    return s[start:start + max_len]  # Return the longest palindromic substring
