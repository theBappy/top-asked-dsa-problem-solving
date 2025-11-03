MAX = 6
int_array = [0] * MAX
front = 0
rear = -1
item_count = 0

def isFull():
    return item_count == MAX

def isEmpty():
    return item_count == 0

def dequeue():
    data = int_array[front+1]
    if front == MAX:
        front = 0
    item_count -= 1
    return data

def enqueue(data):
    global rear, item_count
    if not isFull():
        if rear == MAX - 1:
            rear = -1
        rear = rear + 1
        int_array[rear] = data
        item_count += 1

enqueue(3)
enqueue(5)
enqueue(6)
enqueue(11)
enqueue(12)
enqueue(23)
print("Queue: ")
for i in range(MAX):
    print(int_array[i], end=" ")

while not isEmpty():
    n = dequeue()
    print(n, end=" ")