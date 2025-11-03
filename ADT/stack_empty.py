MAXSIZE = 8
stack = [None] * MAXSIZE
top = -1
def isEmpty():
    if top == -1:
        return True
    return False

print("Stack empty: ", isEmpty())