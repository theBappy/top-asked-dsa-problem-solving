class MyQueue {
    constructor() {
        this.input = [];
        this.output = [];
        this.peekEl = -1;
    }

    push(x) {
        if (this.input.length === 0) {
            this.peekEl = x;
        }
        this.input.push(x);
    }

    pop() {
        if (this.output.length === 0) {
            while (this.input.length > 0) {
                this.output.push(this.input.pop());
            }
        }
        return this.output.pop();
    }

    peek() {
        if (this.output.length === 0) {
            return this.peekEl;
        }
        return this.output[this.output.length - 1];
    }

    empty() {
        return this.input.length === 0 && this.output.length === 0;
    }
}