

def transform(s):
    temp = ['#']
    for ch in s:
        temp.append(ch)
        temp.append('#')
    return ''.join(temp)

    t = transform(s)
    n = len(t)
    l = 0
    r = 0
    center = 0
    max_len = 0
    p = [0] * n

    for i in range(1, n):
        if i > r:
            k = 0
        else:
            j = l + (r - i)
            if j - p[j] > l:
                p[i] = p[j]
                continue
            else:
                k = r - i
        while i - k >= 0 and i + k < n and t[i-1] == t[i+k]:
            k += 1
        k -= 1

        p[i] = k

        if p[i] > max_len:
            max_len = p[i]
            center = i

        if i + k > r:
            l = i - k 
            r = i + k

    start = (center - max_len) // 2
    return s[start: start + max_len]