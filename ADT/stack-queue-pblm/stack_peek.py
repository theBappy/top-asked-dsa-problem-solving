MAXSIZE = 8
stack = [0] * MAXSIZE
top = -1

def isFull():
    if top == MAXSIZE:
        return 1
    else:
        return 0
    
def peek():
    return stack[top]

def push(data):
    global top
    if isFull() != -1:
        top = top + 1
        stack[top] = data
    else:
        print("Stack is full")
    return data

push(44)
push(89)
push(46)
push(34)
push(23)
push(144)

print("Stack elements: ")
for i in range(MAXSIZE):
    print(stack[i], end=" ")

print("\nElement at the top of the stack: ", peek())