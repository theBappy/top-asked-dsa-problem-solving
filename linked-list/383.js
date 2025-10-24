var Solution = function(head) {
    this.arr = []
    let temp = head
    while(temp){
        this.arr.push(temp.val)
        temp = temp.next
    }
};

Solution.prototype.getRandom = function() {
    const n = this.arr.length
    const randomIndex = Math.floor(Math.random() * n)
    return this.arr[randomIndex]
};

