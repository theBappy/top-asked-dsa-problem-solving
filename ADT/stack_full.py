MAXSIZE = 8
stack = [None] * MAXSIZE
top = -1

def isFull():
    if top == MAXSIZE - 1:
        return True
    return False

print("Stack full: ",isFull())