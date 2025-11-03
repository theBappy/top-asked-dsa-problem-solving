MAXSIZE = 8
stack = [0] * MAXSIZE
top = -1

def isEmpty():
    if top == -1:
        return 1
    return 0

def isFull():
    if top == MAXSIZE:
        return 1
    return 0

def peek():
    return stack[top]

def pop():
    global data, top
    if isEmpty() != -1:
        data = stack[top]
        top = top - 1
        return data
    else:
        print("Stack is empty!")

    return data

def push(data):
    global top
    if isFull() != -1:
        top = top + 1
        stack[top] = data
    else:
        print("Stack is full!")
    return data

push(44)
push(10)
push(62)
push(123)
push(15)

print("Element at top of the stack: ", peek())

while isEmpty() != -1:
    data = pop()
    print(data, end=" ")

print("\nStack full: ", bool({True: 1, False: 0} [isFull() == 1]))
print("\nStack empty: ", bool({True: 1, False: 0} [isEmpty() == 1]))