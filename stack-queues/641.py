# In circular nature data structure
# k = maximum size of the element
# increment = ( +1 ) % k
# decrement = ( -1 + k ) % k
# insertFront = (front - 1 + k) % k
# insertRear = (rear + 1) % k
# currentSize should always be considered not more than k ever
# vector <int> deque(k)
# front = 0
# rear = k -1
# currentCount = 0
# deleteFront = (front + 1) % k (increasing index)
# deleteRear = (rear - 1 + k) % k (decreasing index)
# if(currentCount == k) return True (isFull)
# if(currentCount == 0) return True (isEmpty)

##### getFront
# if currentCount == 0 return -1
# else deque[front]

##### getLast
# if currentCount == 0 return -1
# else deque[rear]
# All operations -> TC = O(n) only the constructor will take O(k)
# Sc = O(k) [vector array initialization for k elements]

class MyCircularDeque:
    def __init__(self, k: int):
        self.deq = [0] * k
        self.K = k
        self.front = 0
        self.rear = k - 1
        self.currentCount = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.K) % self.K
        self.deq[self.front] = value
        self.currentCount += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.K
        self.deq[self.rear] = value
        self.currentCount += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.K
        self.currentCount -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.K) % self.K
        self.currentCount -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deq[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deq[self.rear]

    def isEmpty(self) -> bool:
        return self.currentCount == 0

    def isFull(self) -> bool:
        return self.currentCount == self.K
        