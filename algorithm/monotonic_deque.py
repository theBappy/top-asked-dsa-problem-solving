from collections import deque
def monotonic_decreasing_queue(arr, n):
    q = deque()
    for i in range(n):
        while len(q) > 0 and q[-1] > arr[i]:
            q.pop()
        q.append(arr[i])
    return q