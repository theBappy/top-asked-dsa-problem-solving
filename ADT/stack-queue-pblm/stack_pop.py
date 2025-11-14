MAXSIZE = 8
stack = [0] * MAXSIZE
top = -1
def isempty():
    if(top == -1):
        return 1
    else:
        return 0
def isfull():
    if(top == MAXSIZE):
        return 1
    else:
        return 0
def pop():
    global top
    data = 0
    if(isempty() != 1):
        data = stack[top]
        top = top - 1
        return data
    else:
        print("Could not retrieve data, Stack is empty.")
    return data
def push(data):
    global top
    if(isfull() != 1):
        top = top + 1
        stack[top] = data
    else:
        print("\nCould not insert data, Stack is full.")
    return data
push(44)
push(10)
push(62)
push(123)
push(15)
print("Stack Elements: ")
for i in range (MAXSIZE):
    print(stack[i], end = " ")
    
print("\nElements popped: ")
while(isempty() != 1):
    data = pop()
    print(data, end = " ")