class MyCircularDeque {
    constructor(k) {
        this.deq = new Array(k).fill(0);
        this.K = k;
        this.front = 0;
        this.rear = k - 1;
        this.currentCount = 0;
    }

    insertFront(value) {
        if (this.isFull()) {
            return false;
        }
        this.front = (this.front - 1 + this.K) % this.K;
        this.deq[this.front] = value;
        this.currentCount += 1;
        return true;
    }

    insertLast(value) {
        if (this.isFull()) {
            return false;
        }
        this.rear = (this.rear + 1) % this.K;
        this.deq[this.rear] = value;
        this.currentCount += 1;
        return true;
    }

    deleteFront() {
        if (this.isEmpty()) {
            return false;
        }
        this.front = (this.front + 1) % this.K;
        this.currentCount -= 1;
        return true;
    }

    deleteLast() {
        if (this.isEmpty()) {
            return false;
        }
        this.rear = (this.rear - 1 + this.K) % this.K;
        this.currentCount -= 1;
        return true;
    }

    getFront() {
        if (this.isEmpty()) {
            return -1;
        }
        return this.deq[this.front];
    }

    getRear() {
        if (this.isEmpty()) {
            return -1;
        }
        return this.deq[this.rear];
    }

    isEmpty() {
        return this.currentCount === 0;
    }

    isFull() {
        return this.currentCount === this.K;
    }
}